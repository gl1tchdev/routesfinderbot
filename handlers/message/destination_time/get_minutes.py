import telebot.types
from telebot.async_telebot import AsyncTeleBot
from handlers.message import prev
from handlers.message.destination_time import get_answer
from handlers.message.ask_station import prompt
from handlers.message import repeat
from db.crud import get_last_choice, session_db
from db.models import StationType

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    minutes = message.text
    if not minutes.isdigit():
        await bot.reply_to(message, 'Некорректный ввод. Возврат к предыдущему шагу')
        await get_answer.callback(message, bot)
        return
    minutes = int(minutes)
    last_choice = get_last_choice(message.chat.id)
    last_choice.destination_time = minutes
    session_db.commit()
    await bot.send_message(message.chat.id, 'Время установлено')
    if last_choice.station_type == StationType.NODE:
        await repeat.callback(message, bot)
    else:
        await prompt.callback(message, bot)


kwargs = {
    'func': prev(get_answer)
}
