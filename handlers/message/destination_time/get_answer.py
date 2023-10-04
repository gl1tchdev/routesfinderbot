import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import DESTINATION_TIME_ANSWERS
from templates.message import DESTINATION_TIME_INPUT
from db.crud import get_last_choice, StationType
from handlers.message import repeat
from handlers.message.ask_station import prompt

enabled = True

message_text = DESTINATION_TIME_INPUT


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    last_choice = get_last_choice(message.chat.id)
    if message.text == DESTINATION_TIME_ANSWERS[1]:
        if last_choice.station_type == StationType.NODE or last_choice.station_type == StationType.END:
            await repeat.callback(message, bot)
        else:
            await prompt.callback(message, bot)
        return
    force_reply = telebot.types.ForceReply(selective=True)
    await bot.send_message(message.chat.id, text=DESTINATION_TIME_INPUT, reply_markup=force_reply)


kwargs = {
    'func': lambda message: any(message.text == val for val in DESTINATION_TIME_ANSWERS)
}
