from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8253920190:AAGi6X2rCPZ0sU_q8prGZP-8OzUsCbZaCmE"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Купить SeliWare"],
        ["ОПИСАНИЕ"]
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Привет! Нажми кнопку ниже 👇",
        reply_markup=reply_markup
    )

# текстовые кнопки
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "ОПИСАНИЕ":
        await update.message.reply_text(
            "при покупке мы даём вас гарантию на неделю @Ragfa9"
        )

    elif text == "Купить SeliWare":
        await update.message.reply_text(
            "Привет, у него @DollarWare ты можешь купить SeliWare по низкой цене"
        )

    else:
        await update.message.reply_text(
            "Нажми кнопку 👇"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
