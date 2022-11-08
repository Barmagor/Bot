import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update, context):
    with open("text.csv", 'a', encoding='utf-8') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.datetime.now().time()}\n')