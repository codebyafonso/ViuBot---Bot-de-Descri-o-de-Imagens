import base64
import time
import requests
from src.utils import logger
from src.config import OPENROUTER_API_KEY, OPENROUTER_API_URL, OPENROUTER_MODEL
from .chat_service import chat_about_image


def describe_image(image_bytes: bytes, style: str = 'objective') -> str | None:
    """
    Envia os bytes da imagem para a API do OpenRouter para descrição.
    
    Args:
        image_bytes: Bytes da imagem
        style: Estilo de descrição ('detailed', 'quick', 'objective', 'creative')
    """
    if not OPENROUTER_API_KEY:
        return "Erro: Chave de API do OpenRouter não configurada."

    # Define o prompt baseado no estilo
    prompts = {
        'detailed': (
            "Descreva esta imagem em português de forma muito detalhada. "
            "Inclua todos os elementos visíveis, cores, texturas, posições, "
            "atmosfera e qualquer detalhe relevante."
        ),
        'quick': (
            "Descreva esta imagem em português de forma breve e direta. "
            "Máximo 2-3 frases curtas com o essencial."
        ),
        'objective': (
            "Descreva esta imagem em português de forma clara e objetiva. "
            "Foque nos elementos principais: o que você vê, onde está, "
            "quem ou o que aparece. Use parágrafos curtos."
        ),
        'creative': (
            "Descreva esta imagem em português de forma criativa e expressiva. "
            "Use linguagem rica e envolvente, criando uma narrativa visual."
        )
    }
    
    prompt = prompts.get(style, prompts['objective'])
    
    # Converte a imagem para base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/telegram-image-bot",
        "X-Title": "Telegram Image Bot"
    }

    # Define max_tokens baseado no estilo
    max_tokens = {
        'detailed': 800,
        'quick': 150,
        'objective': 400,
        'creative': 600
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "max_tokens": max_tokens.get(style, 400)
    }

    # Retry com backoff exponencial
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=30)
            
            # Se for 429, aguarda e tenta novamente
            if response.status_code == 429:
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2
                    logger.warning(f"Rate limit atingido. Aguardando {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    return "⏳ Limite de requisições atingido. Aguarde alguns segundos e tente novamente."
            
            response.raise_for_status()
            result = response.json()
            
            if 'choices' in result and len(result['choices']) > 0:
                return result['choices'][0]['message']['content']
            elif 'error' in result:
                error_msg = result['error'].get('message', result['error'])
                return f"Erro da API: {error_msg}"
            else:
                logger.error(f"Resposta inesperada da API: {result}")
                return "Erro: Resposta inesperada do serviço de descrição de imagens."

        except requests.exceptions.Timeout:
            logger.error("Timeout na requisição")
            return "⏱️ Tempo limite excedido. Tente novamente."
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro de requisição HTTP: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return f"Erro de conexão: {str(e)}"
        except Exception as e:
            logger.error(f"Erro inesperado na descrição da imagem: {e}")
            return f"Erro interno: {str(e)}"
    
    return "Erro ao processar a imagem após múltiplas tentativas."
