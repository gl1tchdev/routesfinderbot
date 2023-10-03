from typing import Dict
from telebot.types import InlineKeyboardMarkup
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
