from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra opções de configuração do bot."""
    keyboard = [
        [
            InlineKeyboardButton("📝 Descrição Detalhada", callback_data="style_detailed"),
            InlineKeyboardButton("⚡ Descrição Rápida", callback_data="style_quick")
        ],
        [
            InlineKeyboardButton("🎯 Descrição Objetiva", callback_data="style_objective"),
            InlineKeyboardButton("🎨 Descrição Criativa", callback_data="style_creative")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    current_style = context.user_data.get('description_style', 'objective')
    style_names = {
        'detailed': 'Detalhada',
        'quick': 'Rápida',
        'objective': 'Objetiva',
        'creative': 'Criativa'
    }
    
    await update.message.reply_html(
        f"⚙️ <b>Configurações do ViuBot</b>\n\n"
        f"📊 Estilo atual: <b>{style_names.get(current_style, 'Objetiva')}</b>\n\n"
        f"Escolha o estilo de descrição que prefere:",
        reply_markup=reply_markup
    )


async def handle_style_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Processa a escolha de estilo de descrição."""
    query = update.callback_query
    await query.answer()
    
    style = query.data.replace('style_', '')
    context.user_data['description_style'] = style
    
    style_descriptions = {
        'detailed': '📝 Descrições longas e detalhadas com todos os elementos',
        'quick': '⚡ Descrições curtas e diretas ao ponto',
        'objective': '🎯 Descrições claras focando no essencial',
        'creative': '🎨 Descrições mais elaboradas e expressivas'
    }
    
    await query.edit_message_text(
        f"✅ Estilo alterado!\n\n"
        f"{style_descriptions.get(style, '')}\n\n"
        f"Envie uma foto para testar!"
    )
