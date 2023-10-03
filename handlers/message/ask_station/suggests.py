import telebot.types
from telebot.async_telebot import AsyncTeleBot
from db.crud import create_station, get_last_choice
from db.models import StationType
from templates.message import STATION_QUESTIONS, NOT_FOUND
from templates.keyboard import station_choose
from API.yandex import get_suggests
from handlers.message.ask_station import prompt

enabled = True


def trigger(message: telebot.types.Message) -> bool:
    if not message.reply_to_message:
        return False
    return any(value == message.reply_to_message.text for value in STATION_QUESTIONS.values())


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    suggests = get_suggests(message.text)
    if not suggests:
        await bot.send_message(message.chat.id, NOT_FOUND)
        await prompt.callback(message, bot)
        return
    stations = {}
    for suggest in suggests:
        station = create_station(suggest[1], suggest[2], suggest[0])
        stations.update({station.code: station.full_name})
    last_choice = get_last_choice(message.chat.id)
    st_type = last_choice.station_type.next() if last_choice else StationType.START
    markup = station_choose(stations, st_type.value)
    await bot.send_message(message.chat.id, f'Выбери станцию ({st_type.translate().lower()})', reply_markup=markup)


kwargs = {
    'func': trigger
}
