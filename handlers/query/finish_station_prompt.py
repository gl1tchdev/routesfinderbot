import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.locator import FINISH_PROMPT_STATION
from handlers.message.get_timestamp import ask as timestamp_prompt
from handlers.message.ask_station import prompt as station_prompt
from db.crud import get_session_by_user, session_db

enabled = True

locator = FINISH_PROMPT_STATION


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    choice = query.data.replace(locator, '')
    if choice == 'repeat':
        await station_prompt.callback(query.message, bot)
    else:
        await timestamp_prompt.callback(query.message, bot)
        session = get_session_by_user(query.message.chat.id)
        session.prompt_finished = True
        session_db.commit()
    await bot.delete_message(query.message.chat.id, query.message.id)
    await bot.answer_callback_query(query.id)

kwargs = {
    'func': lambda query: query.data.startswith(locator)
}