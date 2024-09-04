from telebot import TeleBot
from telebot import types
from telebot import custom_filters
from telebot.types import Message
from telebot import formatting
import utils
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import messages
import config


bot = TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, formatting.hbold(messages.start_message), parse_mode="HTML")

@bot.message_handler(commands=["help"])
def help_message(message: types.Message):
    bot.send_message(message.chat.id, messages.help_message)

@bot.message_handler(content_types=["text"])
def send_photo(message: types.Message):
    req = message.text
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_username = message.from_user.username
    user_name = f"first_name: {user_first_name}, last_name: {user_last_name}, user_name: {user_username}"
    is_send = False

    utils.write_log(user_name, user_id, req, chat_id)

    info = utils.send_info(req)
    if info:
        bot.send_message(message.chat.id, info)


    path_discs = utils.create_path_discs(req)
    for x in range(len(path_discs)):
        bot.send_photo(message.chat.id, photo=open(path_discs[x], "rb"))
        is_send = True

    path_discs_video = utils.create_path_discs_video(req)
    for i in range(len(path_discs_video)):
        bot.send_video(message.chat.id, video=open(path_discs_video[i], "rb"))

    path_tyres = utils.create_path_tyres(req)
    for x in range(len(path_tyres)):
        bot.send_photo(message.chat.id, photo=open(path_tyres[x], "rb"))
        is_send = True

    path_other = utils.create_path_other(req)
    for x in range(len(path_other)):
        bot.send_photo(message.chat.id, photo=open(path_other[x], "rb"))
        is_send = True

    if not is_send:
        bot.send_message(message.chat.id, f"Фото {req} - не найдено")

    bot.send_message(message.chat.id, messages.start_message)



if __name__ == "__main__":
    bot.infinity_polling()