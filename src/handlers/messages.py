import base64
from io import BytesIO
from telegram import Update
from telegram.ext import ContextTypes
from src.services import describe_image, chat_about_image


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processa a foto enviada pelo usuário."""
    if not update.message.photo:
        await update.message.reply_text("Por favor, envie uma foto como imagem, não como arquivo.")
        return

    photo_file = await update.message.photo[-1].get_file()
    
    image_bytes = BytesIO()
    await photo_file.download_to_memory(image_bytes)
    image_bytes.seek(0)
    image_data = image_bytes.read()
    
    await update.message.reply_text("📸 Foto recebida! Analisando...")

    # Pega o estilo de descrição preferido do usuário
    style = context.user_data.get('description_style', 'objective')
    
    description = describe_image(image_data, style)

    if description:
        # Salva a imagem e descrição no contexto do usuário para conversas futuras
        context.user_data['last_image'] = base64.b64encode(image_data).decode('utf-8')
        context.user_data['last_description'] = description
        context.user_data['conversation_history'] = []
        
        await update.message.reply_html(
            f"🔍 <b>Descrição:</b>\n\n{description}\n\n"
            f"💬 <i>Você pode fazer perguntas sobre esta imagem!</i>"
        )
    else:
        await update.message.reply_text("❌ Desculpe, não consegui obter uma descrição para esta imagem.")


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processa mensagens de texto do usuário."""
    user_message = update.message.text
    
    # Verifica se há uma imagem no contexto
    if 'last_image' not in context.user_data:
        await update.message.reply_html(
            "📸 <b>Envie uma foto primeiro!</b>\n\n"
            "Depois você pode fazer perguntas sobre ela."
        )
        return
    
    # Envia indicador de digitação
    await update.message.chat.send_action("typing")
    
    # Pega a imagem e histórico
    image_base64 = context.user_data['last_image']
    conversation_history = context.user_data.get('conversation_history', [])
    
    # Chama o serviço de chat
    response = chat_about_image(image_base64, user_message, conversation_history)
    
    if response:
        # Atualiza o histórico
        conversation_history.append({
            'user': user_message,
            'assistant': response
        })
        context.user_data['conversation_history'] = conversation_history[-10:]  # Mantém últimas 10 mensagens
        
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("❌ Desculpe, não consegui processar sua pergunta.")
