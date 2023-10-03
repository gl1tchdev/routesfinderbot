import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.locator import FINAL_CHOICE
from handlers.message import start_calculation
from handlers.message.ask_station import prompt
from db.crud import get_session_by_user, session_db

enabled = True

locator = FINAL_CHOICE


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    choice = query.data.replace(locator, '')
    if choice == 'repeat':
        await prompt.callback(query.message, bot)
    else:
        await start_calculation.callback(query.message, bot)
        session = get_session_by_user(query.message.chat.id)
        session.prompt_finished = True
        session_db.commit()
    await bot.delete_message(query.message.chat.id, query.message.id)
    await bot.answer_callback_query(query.id)

kwargs = {
    'func': lambda query: query.data.startswith(locator)
}