import requests
from src.utils import logger
from src.config import OPENROUTER_API_KEY, OPENROUTER_API_URL, OPENROUTER_MODEL


def chat_about_image(image_base64: str, user_question: str, conversation_history: list) -> str | None:
    """
    Permite conversar sobre uma imagem enviada anteriormente.
    
    Args:
        image_base64: Imagem em base64
        user_question: Pergunta do usuário
        conversation_history: Histórico da conversa
    """
    if not OPENROUTER_API_KEY:
        return "Erro: Chave de API do OpenRouter não configurada."
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/telegram-image-bot",
        "X-Title": "Telegram Image Bot"
    }

    # Constrói as mensagens incluindo o histórico
    messages = []
    
    # Primeira mensagem com a imagem
    messages.append({
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Vou te mostrar uma imagem e depois fazer perguntas sobre ela."
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ]
    })
    
    messages.append({
        "role": "assistant",
        "content": "Entendi! Estou vendo a imagem. Pode fazer suas perguntas."
    })
    
    # Adiciona histórico de conversas anteriores
    for msg in conversation_history:
        messages.append({
            "role": "user",
            "content": msg['user']
        })
        messages.append({
            "role": "assistant",
            "content": msg['assistant']
        })
    
    # Adiciona a pergunta atual
    messages.append({
        "role": "user",
        "content": user_question
    })

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        elif 'error' in result:
            error_msg = result['error'].get('message', result['error'])
            logger.error(f"Erro da API: {error_msg}")
            return "Desculpe, ocorreu um erro ao processar sua pergunta."
        else:
            logger.error(f"Resposta inesperada da API: {result}")
            return "Erro ao processar sua pergunta."

    except requests.exceptions.Timeout:
        logger.error("Timeout na requisição")
        return "⏱️ Tempo limite excedido. Tente novamente."
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de requisição HTTP: {e}")
        return "Erro de conexão. Tente novamente."
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        return "Erro ao processar sua pergunta."
