from pprint import pprint

import telebot.types
from telebot.async_telebot import AsyncTeleBot
from API.yandex import get_suggests
from . import welcome
from ...message import prev

enabled = True


def trigger(message: telebot.types.Message) -> bool:
    if not message.reply_to_message:
        return False
    return message.reply_to_message.text == welcome.message_text


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    suggests = get_suggests(message.text)
    pprint(suggests)
    await bot.send_message(message.chat.id, 'ok')


kwargs = {
    'func': prev(welcome)
}
