import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import STATION_QUESTIONS
from db.crud import get_last_choice
from db.models import StationType

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    last_choice = get_last_choice(message.chat.id)
    st_type = last_choice.station_type.next() if last_choice else StationType.START
    markup = telebot.types.ForceReply(selective=True)
    await bot.send_message(message.chat.id, text=STATION_QUESTIONS[st_type], reply_markup=markup)


kwargs = {
    'commands': ['prompt']
}
