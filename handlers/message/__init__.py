import telebot.types


def prev(module):
    def trigger(message: telebot.types.Message):
        if not message.reply_to_message:
            return False
        return message.reply_to_message.text == module.message_text

    return trigger


def hidden(message: telebot.types.Message):
    return False

