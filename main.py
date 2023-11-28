import telebot
import random
from telebot import types  

bot = telebot.TeleBot('6922742437:AAEnUpJ5NJsCe-WQLdx_TuFKb485UyFeR5o')  


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_sender = types.KeyboardButton("Скинь Рандомное число")
    markup.add(random_sender)
    bot.send_message(message.chat.id, '<b>Генератор Рандома Активирован</b> (бип-пуп-пиип)', parse_mode='html',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])


def first_number_step(message):
    if message.text == 'Скинь Рандомное число':
        msg = bot.send_message(message.chat.id, '1')
        bot.register_next_step_handler(msg, second_number_step)             
    else:
        bot.send_message(message.chat.id, 'Такой команды нет')

def second_number_step(message):
    global NUM_first
    NUM_first = int(message.text)
    msg = bot.send_message(message.chat.id, '1001')
    bot.register_next_step_handler(msg, result_number_step)                 


def result_number_step(message):
    global NUM_second
    NUM_second = int(message.text)
    result(message)                                                          


# Вывод результата (рандом)
def result(message):
    bot.send_message(message.chat.id, 'Случайное число:  ' + str(random.randint(NUM_first, NUM_second)))

bot.polling(none_stop=True) 