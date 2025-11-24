from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem quando o comando /start é emitido."""
    user = update.effective_user
    await update.message.reply_html(
        f"👋 Olá, {user.mention_html()}!\n\n"
        "🤖 Eu sou o <b>ViuBot</b>, seu assistente de descrição de imagens!\n\n"
        "📸 <b>Como usar:</b>\n"
        "• Envie uma foto e eu descreverei o que vejo\n"
        "• Funciono com qualquer tipo de imagem\n"
        "• Minhas descrições são em português\n\n"
        "💡 <b>Comandos disponíveis:</b>\n"
        "/start - Mostra esta mensagem\n"
        "/help - Ajuda rápida\n"
        "/config - Configurar estilo de descrição\n\n"
        "🚀 Pronto para começar? Envie sua primeira foto!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia uma mensagem de ajuda quando o comando /help é emitido."""
    await update.message.reply_html(
        "📖 <b>Como usar o ViuBot:</b>\n\n"
        "1️⃣ Envie uma foto (não como arquivo)\n"
        "2️⃣ Aguarde alguns segundos\n"
        "3️⃣ Receba a descrição detalhada!\n\n"
        "⚠️ <b>Importante:</b>\n"
        "• Envie apenas fotos (não documentos)\n"
        "• Uma foto por vez\n"
        "• Imagens claras têm melhores resultados\n\n"
        "❓ Dúvidas? Use /start para mais informações."
    )
