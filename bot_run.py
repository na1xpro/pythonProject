import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
import random

TOKEN  = '1996688275:AAHPXZ9CQoUHUbt5eIAxScPirRV6gcpMySw'

bot = telebot.TeleBot(TOKEN)

url = 'https://www.rbc.ru/crypto/currency/btcusd'
page = requests.get(url=url).text
soup = BeautifulSoup(page, "html.parser")
bitcoin = soup.find("div", class_='chart__subtitle js-chart-value').text

test = ' '.join(bitcoin.split())

# print(str(test))


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

    item1 = types.KeyboardButton("BTC")
    item2 = types.KeyboardButton("DOG")

    markup.add(item1,item2)

    bot.send_message(message.chat.id,'Hello,'.format(message.from_user),reply_markup = markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == "BTC":
        bot.send_message((message.chat.id, 'Курс биткоина' +test))
bot.polling(none_stop=True)