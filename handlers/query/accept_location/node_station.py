import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.locator import NODE_STATION
from db.models import StationType, SearchSession, Station
from db.crud import get_station_by_code, get_session_by_user, register_station_choice
from handlers.message.nodes import fork

enabled = True

locator = NODE_STATION


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    station_code = query.data.replace(locator, '')
    station: Station = get_station_by_code(station_code)
    search_session: SearchSession = get_session_by_user(query.message.chat.id)
    register_station_choice(station, search_session, StationType.NODE)
    await bot.answer_callback_query(query.id, 'Промежуточная станция выбрана')
    await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.id,
                                text=f'Промежуточная станция: {station.short_name}')
    await fork.callback(query.message, bot)



kwargs = {
    'func': lambda query: query.data.startswith(locator)
}
