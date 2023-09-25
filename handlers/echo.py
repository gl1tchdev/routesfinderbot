import telebot.types
from telebot.async_telebot import AsyncTeleBot


def trigger(message: telebot.types.Message) -> bool:
    return True


async def body(message: telebot.types.Message, bot: AsyncTeleBot):
    await bot.send_message(message.chat.id, message.text)
