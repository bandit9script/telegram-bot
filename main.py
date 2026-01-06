import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# токен берётся из переменной окружения (Railway)
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🛒 Купить SeilWare", callback_data="buy"),
            InlineKeyboardButton("📄 ОПИСАНИЕ", callback_data="desc")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выбери действие:",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "desc":
        await query.message.reply_text(
            "при покупке мы даём вас гарантию на неделю @Ragfa9"
        )

    elif query.data == "buy":
        await query.message.reply_text(
            "Привет, у него @DollarWare\n"
            "ты можешь купить SeliWare по низкой цене"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()

if __name__ == "__main__":
    main()