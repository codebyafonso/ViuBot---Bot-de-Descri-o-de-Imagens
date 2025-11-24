import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler, 
    filters,
    PicklePersistence
)
from src.config import TELEGRAM_BOT_TOKEN
from src.handlers import start, help_command, handle_photo, handle_text, handle_unsupported, settings_command, handle_style_callback
from src.utils import logger

# Cria um servidor Flask simples para o Render detectar
app = Flask(__name__)

@app.route('/')
def home():
    return "ViuBot está online! 🤖", 200

@app.route('/health')
def health():
    return {"status": "healthy", "bot": "running"}, 200


def run_flask():
    """Roda o servidor Flask em uma thread separada."""
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)


def main() -> None:
    """Inicia o bot."""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("O token do bot do Telegram não está configurado. O bot não pode ser iniciado.")
        return

    # Inicia o servidor Flask em uma thread separada (para o Render)
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logger.info("Servidor HTTP iniciado para o Render")

    # Adiciona persistência para salvar configurações dos usuários
    persistence = PicklePersistence(filepath="bot_data.pkl")
    
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).persistence(persistence).build()

    # Comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("config", settings_command))
    
    # Callback handlers para botões
    application.add_handler(CallbackQueryHandler(handle_style_callback, pattern="^style_"))
    
    # Handler de fotos
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, handle_photo))
    
    # Handler de mensagens de texto (conversação sobre imagens)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    # Handler para mensagens não suportadas (deve ser o último)
    application.add_handler(MessageHandler(
        (filters.ALL & ~filters.PHOTO & ~filters.COMMAND & ~filters.TEXT) | filters.Document.ALL,
        handle_unsupported
    ))

    logger.info("Bot iniciado. Pressione Ctrl+C para parar.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
