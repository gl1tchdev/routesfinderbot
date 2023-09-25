import inspect
import os
import sys
from pathlib import Path
from importlib import import_module

from telebot.async_telebot import AsyncTeleBot

from config import HANDLERS_PATH


def get_modules(path: Path = HANDLERS_PATH) -> list:
    modules_list = []
    for module_name in os.listdir(HANDLERS_PATH):
        if os.path.isdir(module_name) or module_name[:-3] == '__init__':
            continue
        module_name = 'handlers.' + module_name[:-3]
        import_module(module_name)
        modules_list.append(module_name)
    return modules_list


def setup_handlers(bot: AsyncTeleBot) -> AsyncTeleBot:
    modules = get_modules()
    for module in modules:
        functions = inspect.getmembers(sys.modules[module], inspect.isfunction)
        bot.register_message_handler(functions[0][-1], func=functions[1][-1], pass_bot=True)
    return bot
