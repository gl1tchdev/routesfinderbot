import telebot.types
from telebot.async_telebot import AsyncTeleBot
from handlers.message.ask_station import prompt

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, text='Привет')
    await prompt.callback(message, bot)


kwargs = {
    'commands': ['start']
}
