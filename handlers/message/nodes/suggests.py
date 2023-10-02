import telebot.types
from telebot.async_telebot import AsyncTeleBot
from ...message import prev
from handlers.message.nodes import prompt
from db.crud import create_station
from API.yandex import get_suggests
from templates.message import NOT_FOUND
from templates.locator import NODE_STATION
from templates.keyboard import station_choose

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
    markup = station_choose(stations, NODE_STATION)
    await bot.send_message(message.chat.id, 'Выбери ПРОМЕЖУТОЧНУЮ станцию', reply_markup=markup)

kwargs = {
    'func': prev(prompt)
}