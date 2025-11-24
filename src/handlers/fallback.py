from telegram import Update
from telegram.ext import ContextTypes


async def handle_unsupported(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde quando o usuário envia algo que não é uma foto."""
    message_type = None
    
    if update.message.document:
        message_type = "documento"
    elif update.message.video:
        message_type = "vídeo"
    elif update.message.audio:
        message_type = "áudio"
    elif update.message.voice:
        message_type = "mensagem de voz"
    elif update.message.sticker:
        message_type = "sticker"
    elif update.message.text:
        message_type = "mensagem de texto"
    else:
        message_type = "tipo de mensagem"
    
    await update.message.reply_html(
        f"❌ Desculpe, não posso processar {message_type}.\n\n"
        "📸 <b>Envie apenas fotos!</b>\n\n"
        "💡 <b>Dica:</b> Ao enviar, certifique-se de que está enviando como <b>foto</b> e não como arquivo/documento.\n\n"
        "Use /help para mais informações."
    )
