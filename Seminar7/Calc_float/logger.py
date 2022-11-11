from datetime import datetime



def sum_logger(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}         {} + {} = {} \n". format(time, data1, data2, data3))

def div_logger(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}        {} / {} = {} \n". format(time, data1, data2, data3))


def sub_logger(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}            {} - {} = {} \n". format(time, data1, data2, data3))


def mult_logger(data1, data2, data3):
    time=datetime.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write("{}      {} * {} = {} \n". format(time, data1, data2, data3))