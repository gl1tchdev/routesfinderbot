from telebot.async_telebot import AsyncTeleBot
from handlers_manager import setup_handlers
from config import TELEGRAM_TOKEN

bot_instance = AsyncTeleBot(TELEGRAM_TOKEN)
async_bot_instance = setup_handlers(bot_instance)
