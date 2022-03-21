# -*- coding: utf-8 -*-
from telebot import types


def keyboard2():
    keyboard = types.InlineKeyboardMarkup()
    key_vovochka = types.InlineKeyboardButton('от Вовочки', callback_data='vovochka')
    key_medezina = types.InlineKeyboardButton('про медицину', callback_data='medezina')
    key_ohota = types.InlineKeyboardButton('охота и отдых', callback_data='ohota')
    key_rzhevskiy = types.InlineKeyboardButton('Ржевский', callback_data='rzhevskiy')
    key_schtirliz = types.InlineKeyboardButton('Штирлиц', callback_data='schtirliz')
    key_menu = types.InlineKeyboardButton('Основное меню', callback_data='menu')
    keyboard.add(key_vovochka, key_medezina, key_ohota)
    keyboard.add(key_rzhevskiy, key_schtirliz)
    keyboard.add(key_menu)
    return keyboard


def keyboard1():
    keyboard = types.InlineKeyboardMarkup()
    key_anecdote = types.InlineKeyboardButton('Анекдоты', callback_data='anecdote')
    key_aphorism = types.InlineKeyboardButton('Афоризмы', callback_data='aphorism')
    keyboard.add(key_anecdote, key_aphorism)
    key_toast = types.InlineKeyboardButton('Тосты', callback_data='toast')
    keyboard.add(key_toast)
    return keyboard


def keyboard3():
    keyboard = types.InlineKeyboardMarkup()
    key_woman = types.InlineKeyboardButton('Женские', callback_data='woman')
    key_man = types.InlineKeyboardButton('Мужские', callback_data='man')
    key_wedding = types.InlineKeyboardButton('Свадебные', callback_data='wedding')
    key_fun = types.InlineKeyboardButton('Веселые', callback_data='fun')
    key_army = types.InlineKeyboardButton('Армейские', callback_data='army')
    key_new_year = types.InlineKeyboardButton('Новый год', callback_data='new_year')
    key_menu = types.InlineKeyboardButton('Основное меню', callback_data='menu')
    keyboard.add(key_woman, key_man, key_wedding)
    keyboard.add(key_fun, key_army, key_new_year)
    keyboard.add(key_menu)
    return keyboard
