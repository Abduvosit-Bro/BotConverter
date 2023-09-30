import telebot
import requests

bot = telebot.TeleBot("6097589924:AAEu3UTzRMP1Vzl315OqPHDx1IclIlf15tE")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я конвертирую валюты. Введите сумму:")


@bot.message_handler(content_types=['text'])
def convert(message):
    amount = float(message.text)

    r = requests.get(f'https://api.exchangerate-api.com/v4/latest/RUB').json()
    eur = round(amount / r['rates']['EUR'], 2)
    usd = round(amount / r['rates']['USD'], 2)
    rub = round(amount * r['rates']['RUB'], 2)

    text = f'Это эквивалентно:\n{eur} EUR\n{usd} USD\n{rub} RUB'
    bot.send_message(message.chat.id, text)


bot.polling()