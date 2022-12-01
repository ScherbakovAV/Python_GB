import telebot
from logger import logger

token = '5981421814:AAH7bwtHhZsHp7JTTj0lxgyv4JTf7Aqi0Z4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start(message):

    bot.send_message(message.chat.id, 'Введите выражение для расчёта')

@bot.message_handler(func = lambda message: True)
def answer_to_user(message):

    msg = message.text.replace(' ', '')

    try:
        answer = str(eval(msg))
        result = f'{msg} = {answer}'
        logger(result)
        bot.send_message(message.chat.id, result)         
    except:
        bot.send_message(message.chat.id, 'Ошибка! Повторите ввод...')
    

bot.polling(non_stop=True)
