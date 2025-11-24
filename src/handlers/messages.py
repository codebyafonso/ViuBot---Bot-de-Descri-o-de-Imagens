from io import BytesIO
from telegram import Update
from telegram.ext import ContextTypes
from src.services import describe_image


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processa a foto enviada pelo usuário."""
    if not update.message.photo:
        await update.message.reply_text("Por favor, envie uma foto como imagem, não como arquivo.")
        return

    photo_file = await update.message.photo[-1].get_file()
    
    image_bytes = BytesIO()
    await photo_file.download_to_memory(image_bytes)
    image_bytes.seek(0)
    
    await update.message.reply_text("📸 Foto recebida! Analisando...")

    # Pega o estilo de descrição preferido do usuário
    style = context.user_data.get('description_style', 'objective')
    
    description = describe_image(image_bytes.read(), style)

    if description:
        await update.message.reply_text(f"🔍 <b>Descrição:</b>\n\n{description}", parse_mode='HTML')
    else:
        await update.message.reply_text("❌ Desculpe, não consegui obter uma descrição para esta imagem.")
