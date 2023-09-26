import os
from importlib import import_module

from telebot.async_telebot import AsyncTeleBot

from config import HANDLERS_PATH


def load_handler_modules(handler_type: str) -> dict:
    modules_abs_path = HANDLERS_PATH.joinpath(handler_type)
    modules_dict = {}
    for module_name in os.listdir(modules_abs_path):
        if module_name.startswith('__'):
            continue
        module_name = f'handlers.{handler_type}.' + module_name[:-3]
        module = import_module(module_name)
        modules_dict.update({module_name: module})
    return modules_dict


def setup_handlers(bot: AsyncTeleBot) -> AsyncTeleBot:
    message_handlers = load_handler_modules('message')
    for _, message_handler_module in message_handlers.items():
        if not message_handler_module.enabled:
            continue
        bot.register_message_handler(pass_bot=True, callback=message_handler_module.callback, **message_handler_module.kwargs)

    query_handlers = load_handler_modules('query')
    for _, query_handler_module in query_handlers.items():
        if not query_handler_module.enabled:
            continue
        bot.register_callback_query_handler(pass_bot=True, callback=query_handler_module.callback, **query_handler_module.kwargs)
    return bot



'''
    Params for handler module args:
    
    :param callback: function to be called
    :type callback: :obj:`Awaitable`

    :param content_types: Supported message content types. Must be a list. Defaults to ['text'].
    :type content_types: :obj:`list` of :obj:`str`

    :param commands: list of commands
    :type commands: :obj:`list` of :obj:`str`

    :param regexp:
    :type regexp: :obj:`str`

    :param func: Function executed as a filter
    :type func: :obj:`function`

    :param chat_types: List of chat types
    :type chat_types: :obj:`list` of :obj:`str`

    :param kwargs: Optional keyword arguments(custom filters)
'''
