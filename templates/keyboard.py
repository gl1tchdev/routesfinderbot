from typing import Dict, List
from telebot.types import InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telebot.util import quick_markup
from templates.locator import delimiter


def station_choose(suggests: Dict[str, str], locator: str) -> InlineKeyboardMarkup:
    markup = {}
    for key, value in suggests.items():
        markup.update({
            value: {
                'callback_data': locator + delimiter + key
            }
        })
    return quick_markup(markup, row_width=1)


def get_reply_markup(answers: List[str]) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup()
    for answer in answers:
        button = KeyboardButton(answer)
        markup.add(button)
    return markup
