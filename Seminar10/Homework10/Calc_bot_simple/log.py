from datetime import datetime

def logger(text, file):

    time = datetime.now().strftime("%d.%m.%Y (%H:%M:%S)")
    with open(file, 'a', encoding="utf-8") as file:
        file.write(f'{time}: {text}\n')

def show_log(file):
    logger = ''
    with open(file, 'r', encoding="utf-8") as file:
        for line in file:
            logger += line
    return logger