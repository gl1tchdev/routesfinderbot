import telebot.types
from telebot.async_telebot import AsyncTeleBot
from handlers.message import hidden
from templates.message import DESTINATION_TIME_QUESTION, DESTINATION_TIME_ANSWERS

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.add(telebot.types.KeyboardButton(DESTINATION_TIME_ANSWERS[0]))
    keyboard.add(telebot.types.KeyboardButton(DESTINATION_TIME_ANSWERS[1]))
    await bot.send_message(message.chat.id, DESTINATION_TIME_QUESTION, reply_markup=keyboard)

kwargs = {
    'func': hidden()
}