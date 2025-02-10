from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')

app = Application.builder().token(BOT_TOKEN).build()

async def reply_with_chat_id(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    await update.message.reply_text(str(chat_id), parse_mode="Markdown")

app.add_handler(MessageHandler(filters.ALL, reply_with_chat_id))

if __name__ == "__main__":
    app.run_polling()
