import telebot.types
from telebot.async_telebot import AsyncTeleBot
from db.crud import get_station_by_code, register_station_choice, create_search_session
from db.models import Station, StationType, SearchSession, StationChoice
from templates.locator import START_STATION
from handlers.message.end_location import prompt

enabled = True

locator = START_STATION


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    station_code = query.data.replace(locator, '')
    station: Station = get_station_by_code(station_code)
    search_session: SearchSession = create_search_session(user_id=query.message.chat.id)
    choice: StationChoice = register_station_choice(station, search_session, StationType.START)
    await bot.answer_callback_query(query.id, 'Стартовая станция выбрана')
    await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=f'Старт: {station.short_name}')
    await prompt.callback(query.message, bot)


kwargs = {
    'func': lambda query: query.data.startswith(locator)
}
