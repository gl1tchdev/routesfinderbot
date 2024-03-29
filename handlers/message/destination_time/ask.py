import telebot.types
from telebot.async_telebot import AsyncTeleBot
from handlers.message import hidden
from templates.message import DESTINATION_TIME_QUESTION, DESTINATION_TIME_ANSWERS
from templates.keyboard import get_reply_markup

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    keyboard = get_reply_markup(DESTINATION_TIME_ANSWERS)
    await bot.send_message(message.chat.id, DESTINATION_TIME_QUESTION, reply_markup=keyboard)

kwargs = {
    'func': hidden
}