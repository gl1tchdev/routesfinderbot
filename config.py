import os
from pathlib import Path

HANDLERS_PATH = Path(__file__).resolve().parent.joinpath('handlers')
TELEGRAM_TOKEN = os.environ.get('TG_TOKEN')

# Uncomment if use celery
# from telebot import TeleBot
# sync_bot_instance = TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')