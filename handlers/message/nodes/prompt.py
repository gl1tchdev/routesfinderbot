import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import NODES_STATION
from handlers.message import hidden

enabled = True

message_text = NODES_STATION


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    markup = telebot.types.ForceReply(selective=True)
    await bot.send_message(message.chat.id, text=NODES_STATION, reply_markup=markup)


kwargs = {
    'func': hidden()
}
