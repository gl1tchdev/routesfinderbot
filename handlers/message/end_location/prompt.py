import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import END_STATION
from telebot.types import ForceReply
from ...message import hidden

enabled = True

message_text = END_STATION


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    markup = ForceReply(selective=True)
    await bot.send_message(message.chat.id, text=message_text, reply_markup=markup)


kwargs = {
    'func': hidden()
}
