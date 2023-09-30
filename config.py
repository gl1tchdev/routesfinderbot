import os
from pathlib import Path

HANDLERS_PATH = Path(__file__).resolve().parent.joinpath('handlers')
DB_PATH = Path(__file__).resolve().parent.joinpath('db').joinpath('db.sql')
TELEGRAM_TOKEN = os.environ.get('TG_TOKEN')
RASP_YANDEX_TOKEN = os.environ.get('RASP_YA_TOKEN')

# Uncomment if use celery
# from telebot import TeleBot
# sync_bot_instance = TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')