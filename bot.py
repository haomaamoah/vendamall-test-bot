import os

import telebot

BOT_TOKEN = "6176403772:AAHJScm24E1hkb5tJqR5cTkYlMzXp1KawhY"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, Welcome to VendaMall!\nHow may we assist you?\n"
                          "/start - To begin chat\n"
                          "/enquiry - Request for information\n"
                          "/agent - Talk to Agent\n")

@bot.message_handler(commands=['enquiry'])
def send_welcome(message):
    bot.reply_to(message, "To make enquires, send mail to Vendamall@gmail.com\nHow may we assist you?")

@bot.message_handler(commands=['agent'])
def send_welcome(message):
    bot.reply_to(message, "Our MTN line is 0241234567\nOur Vodafone line is 0201234567\nHow may we assist you?")

@bot.message_handler(commands=['finished'])
def send_welcome(message):
    bot.reply_to(message, "Thank you for using VendaMall, always at your service!")


#@bot.message_handler(func=lambda msg: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)

bot.infinity_polling()