import telebot.types
from telebot.async_telebot import AsyncTeleBot
from telebot.types import ForceReply

enabled = True

message_text = 'Привет. Введи название стартовой станции (города/жд станции/автобусной станции)'


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    markup = ForceReply(selective=True)
    await bot.send_message(message.chat.id, text=message_text, reply_markup=markup)


kwargs = {
    'commands': ['start']
}
