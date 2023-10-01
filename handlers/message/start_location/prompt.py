import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import START_STATION

enabled = True

message_text = START_STATION


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    markup = telebot.types.ForceReply(selective=True)
    await bot.send_message(message.chat.id, text=START_STATION, reply_markup=markup)


kwargs = {
    'commands': ['init']
}
