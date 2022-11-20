from telegram import Update
from telegram.ext import ContextTypes
import datetime
import spy


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await spy.log_command(update, context)
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await spy.log_command(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n/sum\n')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await spy.log_command(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await spy.log_command(update, context)
    msg = update.message.text
    items = msg.split() # /sum 123 5354
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')