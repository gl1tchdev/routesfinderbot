import telebot.types
from telebot.async_telebot import AsyncTeleBot

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, 'Станции выбраны')

kwargs = {
    'commands': ['abcd']
}