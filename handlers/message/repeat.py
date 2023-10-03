import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.locator import FINAL_CHOICE
from telebot.util import quick_markup
from handlers.message import hidden

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    markup_dict = {
        'Добавить промежуточную станцию': {'callback_data': f'{FINAL_CHOICE}repeat'},
        'Закончить выбор': {'callback_data': f'{FINAL_CHOICE}finish'}
    }
    await bot.send_message(message.chat.id, 'Есть ли промежуточные станции?', reply_markup=quick_markup(markup_dict, row_width=1))


kwargs = {
    'func': hidden()
}
