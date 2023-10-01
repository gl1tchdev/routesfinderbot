import telebot.types
from telebot.async_telebot import AsyncTeleBot
from db.crud import create_station
from telebot.util import quick_markup
from API.yandex import get_suggests
from .. import welcome
from ...message import prev

enabled = True


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    suggests = get_suggests(message.text)
    if not suggests:
        await bot.send_message(message.chat.id, 'Ничего не найдено. Попробуй снова')
        await welcome.callback(message, bot)
        return
    markup = {}

    for suggest in get_suggests(message.text):
        station = create_station(suggest[1], suggest[2], suggest[0])
        markup.update({
            suggest[2]: {
                'callback_data': f'start_station:{suggest[0]}'
            }
        })
    await bot.send_message(message.chat.id, 'Выбери СТАРТОВУЮ станцию', reply_markup=quick_markup(markup, row_width=1))


kwargs = {
    'func': prev(welcome)
}
