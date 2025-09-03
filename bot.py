from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters
from datetime import datetime

def handle_message(update: Update, context):
    # Ambil username atau nama depan
    user = update.message.from_user.username or update.message.from_user.first_name
    text = update.message.text
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # format waktu
    payload = f"{now} | f"{user}: {text}"   # gabungkan user + pesan
    mqtt_client.publish(TOPIC, payload)
    update.message.reply_text("Pesan terkirim ke Web!")

updater = Updater(8231334492:AAExey4xZ8HMKi3JE6hudJzaSSI358HUuVs)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text, handle_message))
updater.start_polling()
updater.idle()
