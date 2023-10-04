import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.locator import FINISH_PROMPT_STATION
from telebot.util import quick_markup
from handlers.message import hidden

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    markup_dict = {
        'Добавить промежуточную станцию': {'callback_data': f'{FINISH_PROMPT_STATION}repeat'},
        'Закончить выбор': {'callback_data': f'{FINISH_PROMPT_STATION}finish'}
    }
    await bot.send_message(message.chat.id, 'Есть ли (еще) промежуточные станции?', reply_markup=quick_markup(markup_dict, row_width=1))


kwargs = {
    'func': hidden
}
