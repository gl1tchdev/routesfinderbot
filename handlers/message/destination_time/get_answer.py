import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import DESTINATION_TIME_ANSWERS
from handlers.message.ask_station import prompt
from templates.message import DESTINATION_TIME_INPUT

enabled = True

message_text = DESTINATION_TIME_INPUT


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    if message.text == DESTINATION_TIME_ANSWERS[1]:
        await prompt.callback(message, bot)
        return
    force_reply = telebot.types.ForceReply(selective=True)
    await bot.send_message(message.chat.id, text=DESTINATION_TIME_INPUT, reply_markup=force_reply)


kwargs = {
    'func': lambda message: any(message.text == val for val in DESTINATION_TIME_ANSWERS)
}
