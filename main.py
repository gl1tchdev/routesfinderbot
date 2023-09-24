import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from handlers_dispatcher import setup_handlers

TELEGRAM_TOKEN = os.environ.get('TG_TOKEN')

bot_instance = AsyncTeleBot(TELEGRAM_TOKEN)
async_bot_instance = setup_handlers(bot_instance)
# Uncomment if need celery
# from telebot import TeleBot
# sync_bot_instance = TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')


if __name__ == '__main__':
    asyncio.run(async_bot_instance.polling())