import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.locator import FINAL_CHOICE
from handlers.message.nodes import prompt
from handlers.message import start_calculation

enabled = True

locator = FINAL_CHOICE


async def callback(query: telebot.types.CallbackQuery, bot: AsyncTeleBot):
    choice = query.data.replace(locator, '')
    if choice == 'repeat':
        await prompt.callback(query.message, bot)
    else:
        await start_calculation.callback(query.message, bot)
    await bot.delete_message(query.message.chat.id, query.message.id)
    await bot.answer_callback_query(query.id)

kwargs = {
    'func': lambda query: query.data.startswith(locator)
}