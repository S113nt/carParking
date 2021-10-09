import sqlite3
from datetime import datetime

# текущие дата и время
current_date = datetime.now().date()
current_time = str(datetime.now().time().hour) + ':' + str(datetime.now().time().minute)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# ЗДЕСЬ ДОЛЖНЫ БЫТЬ МАССИВЫ ДЛЯ ХРАНЕНИЯ (ПОТОМ ПОЙМЕШЬ ЧЕГО)

def insert_into_db(row, spaces_count):
    global current_date, current_time
    for i in range(spaces_count):
        print('Parking space -', i + 1)
        brand, color = input().split()
        values = (row, i + 1, brand, color, current_date, current_time)
        cursor.execute('INSERT INTO parking_space VALUES (?, ?, ?, ?, ?, ?)', values)
        conn.commit()

# для создания файла базы данных и таблицы
# cursor.execute("""CREATE TABLE parking_space
#                 (row integer, col integer, brand text, color text, date text, time text)
#                """)


print('Текущая дата:', current_date, ', время:', current_time)

# начальные значения количества рядов на парковке [19, 10, 17]
# ввод данных в таблицу базы данных при помощи вышеописанной функции
'''print('Запись первого ряда.')
insert_into_db(1, 1)
print('Запись второго ряда.')
insert_into_db(2, 2)
print('Запись третьего ряда..')
insert_into_db(3, 3)'''

# функция вывода данных таблицы
# ПО ИДЕЕ СЕЙЧАС НАДО РЕАЛИЗОВАТЬ ФУНКЦИЮ КОТОРАЯ БЫ ПРОБЕГАЛА ПО ВСЕЙ ПАРКОВКЕ ЗАПИСЫВАЯ В ПЕРЕМЕННЫЕ ДАННЫЕ О КАЖДОМ
# ПАРКОВОЧНОМ МЕСТЕ, ТО ЕСТЬ КАКАЯ МАШИНА ТАМ СТОИТ ЧАЩЕ ВСЕГО
# ДАЛЬШЕ ПРЕДЛАГАЮ ДОБАВЛЯТЬ БОЛЬШЕ ФУНКЦИИ, ТИПА В КАКИЕ ДНИ НЕДЕЛИ ЧАЩЕ СТОИТ И ТАК ДАЛЕЕ
# ТАК ЖЕ ПРОГРАММА ДОЛЖНА ВЫВЕСТИ КАКОЕ ПАРКОВОЧНОЕ МЕСТО НАИБОЛЕЕ ОПТИМАЛЬНО ДЛЯ СТОЯНКИ
# ТО ЕСТЬ КУДА МОЖНО ПОСТАВИТЬ МАШИНУ И ЧТОБЫ ОНА НЕ ЗАНИМАЛА ЧЬЕ ТО МЕСТО И НИКОМУ НЕ МЕШАЛА
# УДАЧИ ТЕБЕ В БЛИЖАЙШЕМ БУДУЩЕМ :) ТЫ МОЛОЛЕЦ
cursor.execute('SELECT * FROM parking_space;')
results = cursor.fetchall()
# начинаю реализовывать вышеописанную функцию

# ОСНОВА ПОЛОЖЕНА
'''for i in range(len(results)):
    for j in range(4):
        print(results[i][j], end=' ')
    print()'''
