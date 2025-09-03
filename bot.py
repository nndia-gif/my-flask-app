from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters

def handle_message(update: Update, context):
    # Ambil username atau nama depan
    user = update.message.from_user.username or update.message.from_user.first_name
    text = update.message.text
    payload = f"{user}: {text}"   # gabungkan user + pesan
    mqtt_client.publish(TOPIC, payload)
    update.message.reply_text("Pesan terkirim ke Web!")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
updater.idle()
