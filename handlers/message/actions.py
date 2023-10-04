import telebot.types
from telebot.async_telebot import AsyncTeleBot
from handlers.message import hidden

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, 'Приступаем к расчету')


kwargs = {
    'func': hidden
}
