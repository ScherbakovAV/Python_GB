import telebot

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ["Start"])
def start(m, res = False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь!')


@bot.message_handler(commands = ["Text"])
def handle_text(message):
    s = message.text
    c = 'абв'
    string = str(filter(lambda text: not c in s, s.split()))
    bot.send_message(s.chat.id, string.text)


bot.polling(none_stop = True, interval = 0)

# для другого api
""" async def edit_txt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_mes = update.message.text
    user_mes = user_mes[5:]
    c = 'абв'
    user_mes = list(filter(lambda user_mes: not c in user_mes, user_mes.split()))
    user_mes = ' '.join(user_mes)

    await update.message.reply_text(user_mes) """
