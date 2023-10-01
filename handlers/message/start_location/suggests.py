import telebot.types
from telebot.async_telebot import AsyncTeleBot
from db.crud import create_station
from templates.message import NOT_FOUND
from templates.keyboard import station_choose
from templates.locator import START_STATION
from API.yandex import get_suggests
from handlers.message import prev
from handlers.message.start_location import prompt

enabled = True


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
    markup = station_choose(stations, START_STATION)
    await bot.send_message(message.chat.id, 'Выбери СТАРТОВУЮ станцию', reply_markup=markup)


kwargs = {
    'func': prev(prompt)
}
