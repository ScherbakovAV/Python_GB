from datetime import datetime

def logger(text):
    time=datetime.now()
    #.strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time}: {text}\n')