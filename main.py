import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

keyboard = [
    ["🟢 Get QR", "💰 Balance"],
    ["💸 Withdrawal Request", "📞 Support"],
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to QR Work Bot! 👋\n\nChoose an option below:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        )
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🟢 Get QR":
        await update.message.reply_text(
            "🟢 QR request system will be added soon."
        )

    elif text == "💰 Balance":
        await update.message.reply_text(
            "💰 Your Balance: ₹0"
        )

    elif text == "💸 Withdrawal Request":
        await update.message.reply_text(
            "💸 Withdrawal Request\n\n"
            "Choose your withdrawal method:\n"
            "💳 UPI\n"
            "📱 QR Code"
        )

    elif text == "📞 Support":
        await update.message.reply_text(
            "📞 Please contact the admin for help."
        )


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler)
    )

    print("Bot is running...")
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
