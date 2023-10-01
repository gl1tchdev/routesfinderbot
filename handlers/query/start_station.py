import telebot.types
from telebot.async_telebot import AsyncTeleBot
from db.crud import get_station_by_code, register_station_choice, create_search_session
from db.models import Station, StationType, SearchSession, StationChoice

enabled = True

locator = 'start_station:'


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    station_code = query.data.replace(locator, '')
    station: Station = get_station_by_code(station_code)
    search_session: SearchSession = create_search_session()
    choice: StationChoice = register_station_choice(station, search_session, StationType.START)
    await bot.answer_callback_query(query.id)


kwargs = {
    'func': lambda query: query.data.startswith(locator)
}
