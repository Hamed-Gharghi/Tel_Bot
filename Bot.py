from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace "YOUR_TOKEN_HERE" with your bot's API token
BOT_TOKEN = "7760529796:AAFzsh6prj66yQF4USYP3hFWp5gE0gAXMQs"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your demo bot. Send me any message!')

# Echo handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot started. Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()
