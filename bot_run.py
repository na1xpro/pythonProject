import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types


TOKEN = '1996688275:AAHPXZ9CQoUHUbt5eIAxScPirRV6gcpMySw'

bot = telebot.TeleBot(TOKEN)

responce_bitcoin = requests.get("https://coinremitter.com/api/v2/get-coin-rate")

data = responce_bitcoin.json()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("BTC")
    item2 = types.KeyboardButton("DOGE")
    item3 = types.KeyboardButton("BCH")
    item4 = types.KeyboardButton("TCN")
    item5 = types.KeyboardButton("DASH")
    item6 = types.KeyboardButton("USDTERC20")
    item7 = types.KeyboardButton("BNB")

    markup.add(item1, item2, item3, item4, item5, item6, item7, )

    bot.send_message(message.chat.id, 'Hello, again!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == "BTC":
        bot.send_message(message.chat.id, data['data']['BTC']['price']).format(message.from_user)
    elif message.text == "LTC":
        bot.send_message(message.chat.id, data['data']['LTC']['price']).format(message.from_user)
    elif message.text == "BCH":
        bot.send_message(message.chat.id, data['data']['BCH']['price']).format(message.from_user)
    elif message.text == "DOGE":
        bot.send_message(message.chat.id, data['data']['DOGE']['price']).format(message.from_user)
    elif message.text == "TCN":
        bot.send_message(message.chat.id, data['data']['TCN']['price']).format(message.from_user)
    elif message.text == "DASH":
        bot.send_message(message.chat.id, data['data']['DASH']['price']).format(message.from_user)
    elif message.text == "USDTERC20":
        bot.send_message(message.chat.id, data['data']['USDTERC20']['price']).format(message.from_user)
    elif message.text == "BNB":
        bot.send_message(message.chat.id, data['data']['BNB']['price']).format(message.from_user)
    else:
        bot.send_message(message.chat.id, f' - невідома валюта! Введіть корректну!').format(message.from_user)



bot.polling(none_stop=True)
