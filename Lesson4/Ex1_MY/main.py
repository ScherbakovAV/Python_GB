# Идея: совместная разработка
# Система собирает информацию с датчиков, в ней есть модуль логирования, который заносит в журнал все обращения к датчикам.
# В системе есть модуль, выполняющий обращения для получения данных с датчиков и модуль генерации html представления.
# Запуск системы осуществляется из головного модуля.

import emul_data
import get_data
import data_log 

file_sensors = 'sensor.txt'
file_log = 'log.txt'

emul_data.emul_sensors(file_sensors)
info_from_sensors = get_data.get_info(file_sensors)
data_log.logging(info_from_sensors, file_log)

""" html представление недоступно на данном уровне знаний """
