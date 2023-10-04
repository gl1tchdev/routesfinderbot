import telebot.types
from telebot.async_telebot import AsyncTeleBot
from handlers.message import hidden
from templates.message import TIMESTAMP_QUESTION, TIMESTAMP_ANSWERS
from templates.keyboard import get_reply_markup

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    keyboard = get_reply_markup(TIMESTAMP_ANSWERS)
    await bot.send_message(message.chat.id, text=TIMESTAMP_QUESTION, reply_markup=keyboard)

kwargs = {
    'func': hidden
}