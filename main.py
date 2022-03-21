# -*- coding: utf-8 -*-
import os
import random
import telebot
from config import *
from formuls import list_faile, list_faile_2, list_faile_3, list_faile_4
import logging
from flask import Flask, request
from keyboard import keyboard1, keyboard2, keyboard3

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

jokes_vovochka = list_faile('file_base/anekdoty/Vovochka.txt')
jokes_medezina = list_faile_2()
jokes_ohota = list_faile_3()
jokes_rjevskiy = list_faile_4('file_base/anekdoty/Rjevskiy.txt')
jokes_schtirliz = list_faile_4('file_base/anekdoty/Schtirliz.txt')
jokes_aforizm = list_faile('file_base/aforizmy/aforizmy.txt')
jokes_zenskie = list_faile('file_base/tost/zenskie.txt')
jokes_men = list_faile('file_base/tost/men.txt')
jokes_svadba = list_faile('file_base/tost/svadba.txt')
jokes_prikol = list_faile('file_base/tost/prikol.txt')
jokes_army = list_faile('file_base/tost/army.txt')
jokes_new_year = list_faile('file_base/tost/noviy_god.txt')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Привет, {0.first_name}! Получи свой анекдот, тост или афоризм на сегодня.'
                                           ' Улыбнись - пусть тебе повезет. Доброго дня! '.format(message.from_user))
    keyboard = keyboard1()
    bot.send_message(message.from_user.id, text='Выбери раздел, который тебя интересует', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "anecdote":
        keyboard = keyboard2()
        bot.send_message(call.message.chat.id, text='Выбери раздел анекдота, который тебя интересует',
                         reply_markup=keyboard)
    elif call.data == "vovochka":
        keyboard = keyboard2()
        bot.send_message(call.from_user.id, random.choice(jokes_vovochka), reply_markup=keyboard)
    elif call.data == "medezina":
        keyboard = keyboard2()
        bot.send_message(call.from_user.id, random.choice(jokes_medezina), reply_markup=keyboard)
    elif call.data == "ohota":
        keyboard = keyboard2()
        bot.send_message(call.from_user.id, random.choice(jokes_ohota), reply_markup=keyboard)
    elif call.data == "rzhevskiy":
        keyboard = keyboard2()
        bot.send_message(call.from_user.id, random.choice(jokes_rjevskiy), reply_markup=keyboard)
    elif call.data == "schtirliz":
        keyboard = keyboard2()
        bot.send_message(call.from_user.id, random.choice(jokes_schtirliz), reply_markup=keyboard)
    elif call.data == "menu":
        keyboard = keyboard1()
        bot.send_message(call.from_user.id, text='Выбери раздел, который тебя интересует', reply_markup=keyboard)
    elif call.data == "aphorism":
        keyboard = keyboard1()
        bot.send_message(call.from_user.id, random.choice(jokes_aforizm), reply_markup=keyboard)
    elif call.data == "toast":
        keyboard = keyboard3()
        bot.send_message(call.message.chat.id, text='Выбери раздел тоста, который тебя интересует',
                         reply_markup=keyboard)
    elif call.data == "woman":
        keyboard = keyboard3()
        bot.send_message(call.from_user.id, random.choice(jokes_zenskie), reply_markup=keyboard)
    elif call.data == "man":
        keyboard = keyboard3()
        bot.send_message(call.from_user.id, random.choice(jokes_men), reply_markup=keyboard)
    elif call.data == "wedding":
        keyboard = keyboard3()
        bot.send_message(call.from_user.id, random.choice(jokes_svadba), reply_markup=keyboard)
    elif call.data == "fun":
        keyboard = keyboard3()
        bot.send_message(call.from_user.id, random.choice(jokes_prikol), reply_markup=keyboard)
    elif call.data == "army":
        keyboard = keyboard3()
        bot.send_message(call.from_user.id, random.choice(jokes_army), reply_markup=keyboard)
    elif call.data == "new_year":
        keyboard = keyboard3()
        bot.send_message(call.from_user.id, random.choice(jokes_new_year), reply_markup=keyboard)


@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
