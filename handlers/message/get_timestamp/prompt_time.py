import telebot.types
from telebot.async_telebot import AsyncTeleBot
from handlers.message import prev
from handlers.message.get_timestamp import get_answer
from handlers.message.get_timestamp import is_input_valid, get_datetime_from_str
from handlers.message import actions
from db.crud import set_session_timestamp

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    input_time = message.text
    if not is_input_valid(input_time):
        await bot.send_message(message.chat.id, 'Неверный формат')
        await get_answer.callback(message, bot)
        return
    timestamp = get_datetime_from_str(input_time)
    set_session_timestamp(message.chat.id, timestamp)
    await bot.send_message(message.chat.id, 'Время успешно указано. Переход к следующему шагу')
    await actions.callback(message, bot)



kwargs = {
    'func': prev(get_answer)
}
