from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from command import *

updater = Updater('5785238718:AAEucu7_2C7F5S5lp1rEyea_UmYt5-SC3fA')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('input', import_names))
updater.dispatcher.add_handler(CommandHandler('found', export))
updater.dispatcher.add_handler(CommandHandler('sort', sort_file))
updater.dispatcher.add_handler(CommandHandler('output', output))

updater.start_polling()
updater.idle()