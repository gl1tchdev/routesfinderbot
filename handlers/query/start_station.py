import telebot.types
from telebot.async_telebot import AsyncTeleBot

enabled = True

locator = 'start_station'


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    await bot.answer_callback_query(query.id, query.data)


kwargs = {
    'func': lambda query: query.data.startswith(locator)
}
