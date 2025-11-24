# 🤖 ViuBot - Bot de Descrição de Imagens

> Um assistente inteligente para o Telegram que descreve suas fotos em português usando inteligência artificial.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 O que é o ViuBot?

O **ViuBot** é um bot do Telegram que analisa suas fotos e cria descrições detalhadas em português. Basta enviar uma imagem e ele te conta o que está vendo - pessoas, lugares, objetos, cores, e muito mais!

### ✨ Para que serve?

- 📸 **Descrever fotos** - Entenda melhor o conteúdo das suas imagens
- 🎨 **Analisar arte** - Obtenha descrições de pinturas e ilustrações
- 🏞️ **Identificar lugares** - Descubra detalhes sobre paisagens e locais
- 👥 **Descrever cenas** - Entenda o contexto de fotos com pessoas e eventos
- ♿ **Acessibilidade** - Ajuda pessoas com deficiência visual a "ver" imagens

---

## 🎯 Como funciona?

1. **Você envia uma foto** para o bot no Telegram
2. **O bot analisa** a imagem usando inteligência artificial
3. **Você recebe** uma descrição detalhada em português

É simples assim! Não precisa de comandos complicados ou configurações técnicas.

---

## 🚀 Começando a usar

### Pré-requisitos

Você vai precisar de:
- Uma conta no [Telegram](https://telegram.org/)
- Uma chave de API do [OpenRouter](https://openrouter.ai/) (gratuita)
- Python 3.9 ou superior instalado no seu computador

### Instalação Rápida

1. **Baixe o projeto**
   ```bash
   git clone https://github.com/codebyafonso/ViuBot---Bot-de-Descri-o-de-Imagens.git
   cd ViuBot---Bot-de-Descri-o-de-Imagens
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure suas chaves**
   - Copie o arquivo `.env.example` para `.env`
   - Adicione seu token do bot do Telegram
   - Adicione sua chave da API do OpenRouter

4. **Inicie o bot**
   ```bash
   python main.py
   ```

Pronto! Seu bot já está funcionando! 🎉

---

## 💬 Comandos disponíveis

| Comando | Descrição |
|---------|-----------|
| `/start` | Inicia o bot e mostra as boas-vindas |
| `/help` | Mostra instruções de uso |
| `/config` | Configura o estilo de descrição |

### 🎨 Estilos de descrição

Você pode escolher como quer que o bot descreva suas fotos:

- **📝 Detalhada** - Descrição completa com todos os detalhes
- **⚡ Rápida** - Apenas o essencial em 2-3 frases
- **🎯 Objetiva** - Equilibrada e clara (padrão)
- **🎨 Criativa** - Descrição mais elaborada e expressiva

Use `/config` para escolher seu estilo preferido!

---

## 📱 Como usar no Telegram

1. **Abra o Telegram** e procure pelo seu bot
2. **Clique em "Iniciar"** ou envie `/start`
3. **Envie uma foto** (não como arquivo/documento)
4. **Aguarde alguns segundos** enquanto a IA analisa
5. **Receba a descrição** em português!

### 💡 Dicas

- ✅ Envie fotos claras e bem iluminadas
- ✅ Uma foto por vez para melhores resultados
- ✅ Funciona com qualquer tipo de imagem
- ❌ Não envie como documento/arquivo
- ❌ Não funciona com vídeos ou áudios

---

## 🛠️ Para desenvolvedores

### Estrutura do projeto

```
telegram-image-bot/
├── src/                    # Código fonte
│   ├── config/            # Configurações
│   ├── handlers/          # Manipuladores de mensagens
│   ├── services/          # Serviços (API de IA)
│   └── utils/             # Utilitários
├── main.py                # Arquivo principal
├── dev.py                 # Modo desenvolvimento
├── requirements.txt       # Dependências
└── .env                   # Configurações (não commitar)
```

### Modo desenvolvimento

Para desenvolver com auto-reload:

```bash
python dev.py
```

O bot reinicia automaticamente quando você modifica o código!

### Tecnologias usadas

- **Python 3.9+** - Linguagem de programação
- **python-telegram-bot** - Framework para bots do Telegram
- **OpenRouter API** - Acesso a modelos de IA
- **Watchdog** - Auto-reload em desenvolvimento

---

## 🔐 Configuração

### Obtendo as chaves necessárias

#### 1. Token do Bot do Telegram

1. Abra o Telegram e procure por [@BotFather](https://t.me/botfather)
2. Envie `/newbot` e siga as instruções
3. Copie o token que ele te enviar
4. Cole no arquivo `.env` em `TELEGRAM_BOT_TOKEN`

#### 2. Chave da API do OpenRouter

1. Acesse [openrouter.ai](https://openrouter.ai/)
2. Crie uma conta gratuita
3. Vá em "Keys" e crie uma nova chave
4. Cole no arquivo `.env` em `OPENROUTER_API_KEY`

### Arquivo .env

```env
TELEGRAM_BOT_TOKEN=seu_token_aqui
OPENROUTER_API_KEY=sua_chave_aqui
OPENROUTER_MODEL=openai/gpt-4o-mini
```

---

## 🎓 Perguntas frequentes

**P: O bot é gratuito?**  
R: Sim! O OpenRouter oferece créditos gratuitos para começar.

**P: Funciona com qualquer tipo de foto?**  
R: Sim! Fotos, ilustrações, capturas de tela, memes, etc.

**P: As descrições são sempre em português?**  
R: Sim, o bot foi configurado para responder sempre em português.

**P: Posso usar em grupos?**  
R: Sim! Adicione o bot ao grupo e mencione ele com as fotos.

**P: Meus dados estão seguros?**  
R: As imagens são processadas pela API e não são armazenadas.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

- 🐛 Reportar bugs
- 💡 Sugerir novas funcionalidades
- 🔧 Enviar pull requests
- 📖 Melhorar a documentação

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 💖 Agradecimentos

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Framework incrível
- [OpenRouter](https://openrouter.ai/) - Acesso simplificado a modelos de IA
- Comunidade Python - Por todas as bibliotecas úteis

---

## 📞 Suporte

Encontrou algum problema? Tem alguma dúvida?

- 📧 Abra uma [issue](https://github.com/codebyafonso/ViuBot---Bot-de-Descri-o-de-Imagens/issues)
- 💬 Entre em contato pelo Telegram: [@codebyafonso](https://t.me/codebyafonso)

---

<div align="center">

**Feito com ❤️ e Python**

⭐ Se você gostou, deixe uma estrela no projeto!

</div>
