from telegram.ext import ApplicationBuilder, CommandHandler
import bot_commands

app = ApplicationBuilder().token('5854719104:AAHFlSEs1bMHtSYw_3BKf6mgcL19s1h7L0I').build()

app.add_handler(CommandHandler("hello", bot_commands.hello_command))
app.add_handler(CommandHandler("time", bot_commands.time_command))
app.add_handler(CommandHandler("help", bot_commands.help_command))
app.add_handler(CommandHandler("sum", bot_commands.sum_command))
print('server start')
app.run_polling()