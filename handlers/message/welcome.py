import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import START_STATION
from handlers.message.start_location import prompt

enabled = True

message_text = START_STATION


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, text='Привет')
    await prompt.callback(message, bot)


kwargs = {
    'commands': ['start']
}
