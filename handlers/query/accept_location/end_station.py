import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.locator import END_STATION
from db.models import Station, StationType, SearchSession
from db.crud import register_station_choice, get_station_by_code, get_session_by_user
from handlers.message.nodes import prompt


enabled = True

locator = END_STATION


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    station_code = query.data.replace(locator, '')
    station: Station = get_station_by_code(station_code)
    search_session: SearchSession = get_session_by_user(query.message.chat.id)
    register_station_choice(station, search_session, StationType.END)
    await bot.answer_callback_query(query.id, 'Конечная станция выбрана')
    await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id, text=f'Конец: {station.short_name}')
    await prompt.callback(query.message, bot)

kwargs = {
    'func': lambda query: query.data.startswith(locator)
}
