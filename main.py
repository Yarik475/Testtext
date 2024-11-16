import telebot
from telebot import types

bot = telebot.Telebot('7221544463:AAHn7hND1VOgX0dNssC5Wxus7dbT6xENMHA')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
services = types.KeyboardButton("Погода")
prices = types.KeyboardButton("Валюта")
contacts = types.KeyboardButton("Выбрать язык")
menu.add(services, prices, contacts)

back = types.ReplyKeyboardMarkup(resize_Keyboard=True)
back_button = types.KeyboardButton("Назад")
back.add(back_button)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")


bot.infinity_polling()
