import telebot
import requests
import os

os.system("pip install requests")
os.system("pip install telebot")

bot = telebot.TeleBot("6438805936:AAHDAxswdZyQVH62kCjAYSSGE36kJf3aT4E")

@bot.message_handler(commands='start')

def start(message):
	bot.send_message(message.chat.id, "Введи команду /phone 79999999999")
	
@bot.message_handler(commands='phone')

def phone(message):
	number = message.text[7:len(message.text)]
	bot.send_message(message.chat.id, "Загружаем результаты:")
	
	results = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key=9e9ee6779b55406aad9fc88becb41f50&phone={number}")
	
	bot.send_message(message.chat.id, results.content)
bot.polling(none_stop=True)
