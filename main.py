import os
import random
import telebot
from telebot import types
from config import *
from formuls import list_faile, list_faile_2, list_faile_3, list_faile_4
import logging
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

# jokes_vovochka = list_faile('file_base/anekdoty/Vovochka.txt')
# jokes_medezina = list_faile_2()
# jokes_ohota = list_faile_3()
# jokes_rjevskiy = list_faile_4('file_base/anekdoty/Rjevskiy.txt')
# jokes_schtirliz = list_faile_4('file_base/anekdoty/Schtirliz.txt')
# jokes_aforizm = list_faile('file_base/aforizmy/aforizmy.txt')
# jokes_zenskie = list_faile('file_base/tost/zenskie.txt')
# jokes_men = list_faile('file_base/tost/men.txt')
# jokes_svadba = list_faile('file_base/tost/svadba.txt')
# jokes_prikol = list_faile('file_base/tost/prikol.txt')
# jokes_army = list_faile('file_base/tost/army.txt')
# jokes_new_year = list_faile('file_base/tost/noviy_god.txt')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='������, {0.first_name}! ������ ���� �������, ���� ��� ������� �� �������.'
                                           ' �������� - ����� ���� �������. ������� ���! '.format(message.from_user))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("��������")
    btn2 = types.KeyboardButton("��������")
    btn3 = types.KeyboardButton("�����")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text='������ ������'.format(message.from_user),
                     reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def func(message):
#     if message.text == "��������":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn3 = types.KeyboardButton("�� �������")
#         btn4 = types.KeyboardButton("��� ��������")
#         btn5 = types.KeyboardButton("����� � �����")
#         btn6 = types.KeyboardButton("��������")
#         btn7 = types.KeyboardButton("�������")
#         back = types.KeyboardButton("�������� ����")
#         markup.add(btn3, btn4, btn5, btn6, btn7, back)
#         bot.send_message(message.chat.id, text="������ ������ ��������", reply_markup=markup)
#     elif message.text == "�����":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn3 = types.KeyboardButton("�������")
#         btn4 = types.KeyboardButton("�������")
#         btn5 = types.KeyboardButton("���������")
#         btn6 = types.KeyboardButton("�������")
#         btn7 = types.KeyboardButton("���������")
#         btn8 = types.KeyboardButton("����� ���")
#         back = types.KeyboardButton("�������� ����")
#         markup.add(btn3, btn4, btn5, btn6, btn7, btn8, back)
#         bot.send_message(message.chat.id, text="������ ������", reply_markup=markup)
#     elif message.text == "�� �������":
#         bot.send_message(message.from_user.id, random.choice(jokes_vovochka))
#     elif message.text == "��� ��������":
#         bot.send_message(message.from_user.id, random.choice(jokes_medezina))
#     elif message.text == "����� � �����":
#         bot.send_message(message.from_user.id, random.choice(jokes_ohota))
#     elif message.text == "��������":
#         bot.send_message(message.from_user.id, random.choice(jokes_rjevskiy))
#     elif message.text == "�������":
#         bot.send_message(message.from_user.id, random.choice(jokes_schtirliz))
#     elif message.text == "��������":
#         bot.send_message(message.from_user.id, random.choice(jokes_aforizm))
#     elif message.text == "�������":
#         bot.send_message(message.from_user.id, random.choice(jokes_zenskie))
#     elif message.text == "�������":
#         bot.send_message(message.from_user.id, random.choice(jokes_men))
#     elif message.text == "���������":
#         bot.send_message(message.from_user.id, random.choice(jokes_svadba))
#     elif message.text == "�������":
#         bot.send_message(message.from_user.id, random.choice(jokes_prikol))
#     elif message.text == "���������":
#         bot.send_message(message.from_user.id, random.choice(jokes_army))
#     elif message.text == "����� ���":
#         bot.send_message(message.from_user.id, random.choice(jokes_new_year))
#     elif message.text == "�������� ����":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("��������")
#         btn2 = types.KeyboardButton("��������")
#         btn3 = types.KeyboardButton("�����")
#         markup.add(btn1, btn2, btn3)
#         bot.send_message(message.chat.id, text="�� ��������� � ������� ����", reply_markup=markup)


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
