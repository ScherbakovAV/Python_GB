import telebot
from random import randint as ran

token = '5984186750:AAE1r20K001kv7qseXCGnSeApFJ2oCLK4Lc'
bot = telebot.TeleBot(token)

candies = 0
max_candies = 28
    
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


@bot.message_handler(commands=["game"])
def handle_text(message):
    global candies
    candies = 101
    bot.send_message(message.chat.id, f'На столе лежит {candies} конфет')
    # game(candies, max_candies)


@bot.message_handler(content_types=["text"])
def inputs(message):
    global candies

    if candies <= 0:
        bot.send_message(message.chat.id, f'Игра окончена')
        handle_text(message)
        return
    else: bot.send_message(message.chat.id, f'Возьмите конфеты:')

    try:
        can = int(message.text)
        candies = candies - can
        bot.send_message(message.chat.id, f'Конфет осталось {candies}')
        ran_can = ran(1, max_candies)
        candies = candies - ran_can
        bot.send_message(message.chat.id, f'Бот взял {ran_can} конфет, их осталось {candies}')
    except ValueError:
        bot.send_message(message.chat.id, f'Ошибка. Введите число...')
        

    # c = list(text1.split())
    # text1 = filter(lambda c: c.isdigit(), c)


bot.polling(none_stop=True, interval=0)
