from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from src.config import TELEGRAM_BOT_TOKEN
from src.handlers import start, help_command, handle_photo, handle_unsupported, settings_command, handle_style_callback
from src.utils import logger


def main() -> None:
    """Inicia o bot."""
    if not TELEGRAM_BOT_TOKEN:
        logger.error("O token do bot do Telegram não está configurado. O bot não pode ser iniciado.")
        return

    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("config", settings_command))
    
    # Callback handlers para botões
    application.add_handler(CallbackQueryHandler(handle_style_callback, pattern="^style_"))
    
    # Handler de fotos
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, handle_photo))
    
    # Handler para mensagens não suportadas (deve ser o último)
    application.add_handler(MessageHandler(
        (filters.ALL & ~filters.PHOTO & ~filters.COMMAND) | filters.Document.ALL,
        handle_unsupported
    ))

    logger.info("Bot iniciado. Pressione Ctrl+C para parar.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
