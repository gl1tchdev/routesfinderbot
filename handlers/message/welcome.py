import telebot.types
from telebot.async_telebot import AsyncTeleBot
from telebot.types import ForceReply

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    text = 'Привет. Введи название стартовой станции (города/жд станции/автобусной станции)'
    markup = ForceReply(selective=True)
    await bot.send_message(message.chat.id, text, reply_markup=markup)


kwargs = {
    'commands': ['start']
}
