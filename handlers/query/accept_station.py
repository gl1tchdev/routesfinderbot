import telebot.types
from telebot.async_telebot import AsyncTeleBot
from db.crud import get_station_by_code, register_station_choice, get_session_by_user, create_search_session
from db.models import Station, StationType, SearchSession, StationChoice
from templates.locator import delimiter
from typing import Optional
from handlers.message import repeat
from handlers.message.destination_time import ask

enabled = True


def trigger(query: telebot.types.CallbackQuery) -> bool:
    return any(query.data.startswith(elem.value) for elem in StationType)


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    station_data = query.data.split(delimiter)
    station_locator = station_data[0]
    station_code = station_data[-1]
    station: Station = get_station_by_code(station_code)
    search_session: Optional[SearchSession] = get_session_by_user(query.message.chat.id)
    if not search_session:
        search_session: SearchSession = create_search_session(user_id=query.message.chat.id)
    st_type = StationType(station_locator)
    choice: StationChoice = register_station_choice(station, search_session, st_type)
    await bot.answer_callback_query(query.id, f'{st_type.translate()} выбрана')
    await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id,
                                text=f'{st_type.translate()}: {station.short_name}')
    if not st_type == StationType.END:
        await ask.callback(query.message, bot)
    else:
        await repeat.callback(query.message, bot)


kwargs = {
    'func': trigger
}
