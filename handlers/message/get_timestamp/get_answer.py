import telebot.types
from telebot.async_telebot import AsyncTeleBot
from templates.message import TIMESTAMP_ANSWERS
from db.crud import set_session_timestamp
from handlers.message.get_timestamp import get_now_datetime
from handlers.message import actions
from templates.message import TIMESTAMP_PROMPT

enabled = True

message_text = TIMESTAMP_PROMPT


def trigger(message: telebot.types.Message) -> bool:
    return any(answer == message.text for answer in TIMESTAMP_ANSWERS)


async def callback(message: telebot.types.Message, bot: AsyncTeleBot):
    if message.text == TIMESTAMP_ANSWERS[0]:
        timestamp = get_now_datetime()
        set_session_timestamp(message.chat.id, timestamp)
        await actions.callback(message, bot)
    else:
        force_reply = telebot.types.ForceReply(selective=True)
        await bot.send_message(message.chat.id, text=TIMESTAMP_PROMPT, reply_markup=force_reply)


kwargs = {
    'func': trigger
}
