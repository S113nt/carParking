import sqlite3
from datetime import datetime

# текущие дата и время
current_date = datetime.now().date()
current_time = str(datetime.now().time().hour) + ':' + str(datetime.now().time().minute)

# связывание с базой данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# ЗДЕСЬ ДОЛЖНЫ БЫТЬ МАССИВЫ ДЛЯ ХРАНЕНИЯ (ПОТОМ ПОЙМЕШЬ ЧЕГО)
space_1_1, space_1_2, space_1_3, space_1_4, space_1_5, space_1_6, space_1_7, space_1_8 = [], [], [], [], [], [], [], []
space_1_9, space_1_10, space_1_11, space_1_12, space_1_13, space_1_14, space_1_15 = [], [], [], [], [], [], []
space_1_16, space_1_17, space_1_18, space_1_19 = [], [], [], [],
space_2_1, space_2_2, space_2_3, space_2_4, space_2_5 = [], [], [], [], []
space_2_6, space_2_7, space_2_8, space_2_9, space_2_10 = [], [], [], [], []
space_3_1, space_3_2, space_3_3, space_3_4, space_3_5, space_3_6, space_3_7, space_3_8 = [], [], [], [], [], [], [], []
space_3_9, space_3_10, space_3_11, space_3_12, space_3_13 = [], [], [], [], []
space_3_14, space_3_15, space_3_16, space_3_17 = [], [], [], []


def insert_into_db(row, spaces_count):
    global current_date, current_time
    for i in range(spaces_count):
        print('Parking space -', i + 1)
        brand, color = input().split()
        values = (row, i + 1, brand, color, current_date, current_time)
        cursor.execute('INSERT INTO parking_space VALUES (?, ?, ?, ?, ?, ?)', values)
        conn.commit()


def print_first_row():
    print('Вывод данных с первого ряда:')
    print(space_1_1)
    print(space_1_2)
    print(space_1_3)
    print(space_1_4)
    print(space_1_5)
    print(space_1_6)
    print(space_1_7)
    print(space_1_8)
    print(space_1_9)
    print(space_1_10)
    print(space_1_11)
    print(space_1_12)
    print(space_1_13)
    print(space_1_14)
    print(space_1_15)
    print(space_1_16)
    print(space_1_17)
    print(space_1_18)
    print(space_1_19)


def print_second_row():
    print('Вывод данных со второго ряда:')
    print(space_2_1)
    print(space_2_2)
    print(space_2_3)
    print(space_2_4)
    print(space_2_5)
    print(space_2_6)
    print(space_2_7)
    print(space_2_8)
    print(space_2_9)
    print(space_2_10)


def print_third_row():
    print('Вывод данных с третьего ряда:')
    print(space_3_1)
    print(space_3_2)
    print(space_3_3)
    print(space_3_4)
    print(space_3_5)
    print(space_3_6)
    print(space_3_7)
    print(space_3_8)
    print(space_3_9)
    print(space_3_10)
    print(space_3_11)
    print(space_3_12)
    print(space_3_13)
    print(space_3_14)
    print(space_3_15)
    print(space_3_16)
    print(space_3_17)


def max_first_row():
    print('Наибольшее количество вхождений по первому ряду:')
    print('1:', max(space_1_1, key=space_1_1.count))
    print('2:', max(space_1_2, key=space_1_2.count))
    print('3:', max(space_1_3, key=space_1_3.count))
    print('4:', max(space_1_4, key=space_1_4.count))
    print('5:', max(space_1_5, key=space_1_5.count))
    print('6:', max(space_1_6, key=space_1_6.count))
    print('7:', max(space_1_7, key=space_1_7.count))
    print('8:', max(space_1_8, key=space_1_8.count))
    print('9:', max(space_1_9, key=space_1_9.count))
    print('10:', max(space_1_10, key=space_1_10.count))
    print('11:', max(space_1_11, key=space_1_11.count))
    print('12:', max(space_1_12, key=space_1_12.count))
    print('13:', max(space_1_13, key=space_1_13.count))
    print('14:', max(space_1_14, key=space_1_14.count))
    print('15:', max(space_1_15, key=space_1_15.count))
    print('16:', max(space_1_16, key=space_1_16.count))
    print('17:', max(space_1_17, key=space_1_17.count))
    print('18:', max(space_1_18, key=space_1_18.count))
    print('19:', max(space_1_19, key=space_1_19.count))


def max_second_row():
    print('Наибольшее количество вхождений по второму ряду:')
    print('1:', max(space_2_1, key=space_2_1.count))
    print('2:', max(space_2_2, key=space_2_2.count))
    print('3:', max(space_2_3, key=space_2_3.count))
    print('4:', max(space_2_4, key=space_2_4.count))
    print('5:', max(space_2_5, key=space_2_5.count))
    print('6:', max(space_2_6, key=space_2_6.count))
    print('7:', max(space_2_7, key=space_2_7.count))
    print('8:', max(space_2_8, key=space_2_8.count))
    print('9:', max(space_2_9, key=space_2_9.count))
    print('10:', max(space_2_10, key=space_2_10.count))


def max_third_row():
    print('Наибольшее количество вхождений по третьему ряду:')
    print('1:', max(space_3_1, key=space_3_1.count))
    print('2:', max(space_3_2, key=space_3_2.count))
    print('3:', max(space_3_3, key=space_3_3.count))
    print('4:', max(space_3_4, key=space_3_4.count))
    print('5:', max(space_3_5, key=space_3_5.count))
    print('6:', max(space_3_6, key=space_3_6.count))
    print('7:', max(space_3_7, key=space_3_7.count))
    print('8:', max(space_3_8, key=space_3_8.count))
    print('9:', max(space_3_9, key=space_3_9.count))
    print('10:', max(space_3_10, key=space_3_10.count))
    print('11:', max(space_3_11, key=space_3_11.count))
    print('12:', max(space_3_12, key=space_3_12.count))
    print('13:', max(space_3_13, key=space_3_13.count))
    print('14:', max(space_3_14, key=space_3_14.count))
    print('15:', max(space_3_15, key=space_3_15.count))
    print('16:', max(space_3_16, key=space_3_16.count))
    print('17:', max(space_3_17, key=space_3_17.count))

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

for i in range(len(results)):
    if results[i][0] == 1:
        if results[i][1] == 1:
            space_1_1.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 2:
            space_1_2.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 3:
            space_1_3.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 4:
            space_1_4.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 5:
            space_1_5.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 6:
            space_1_6.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 7:
            space_1_7.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 8:
            space_1_8.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 9:
            space_1_9.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 10:
            space_1_10.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 11:
            space_1_11.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 12:
            space_1_12.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 13:
            space_1_13.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 14:
            space_1_14.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 15:
            space_1_15.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 16:
            space_1_16.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 17:
            space_1_17.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 18:
            space_1_18.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 19:
            space_1_19.append(results[i][2] + ' ' + results[i][3])
    if results[i][0] == 2:
        if results[i][1] == 1:
            space_2_1.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 2:
            space_2_2.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 3:
            space_2_3.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 4:
            space_2_4.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 5:
            space_2_5.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 6:
            space_2_6.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 7:
            space_2_7.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 8:
            space_2_8.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 9:
            space_2_9.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 10:
            space_2_10.append(results[i][2] + ' ' + results[i][3])
    if results[i][0] == 3:
        if results[i][1] == 1:
            space_3_1.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 2:
            space_3_2.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 3:
            space_3_3.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 4:
            space_3_4.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 5:
            space_3_5.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 6:
            space_3_6.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 7:
            space_3_7.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 8:
            space_3_8.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 9:
            space_3_9.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 10:
            space_3_10.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 11:
            space_3_11.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 12:
            space_3_12.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 13:
            space_3_13.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 14:
            space_3_14.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 15:
            space_3_15.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 16:
            space_3_16.append(results[i][2] + ' ' + results[i][3])
        if results[i][1] == 17:
            space_3_17.append(results[i][2] + ' ' + results[i][3])


# ВСЁ РАБОТАЕТ, НО БЕЗ АВТОМАТИЗАЦИИ ЭТО БЕССМЫСЛЕННО! ОЧЕНЬ НЕ КРАСИВО И Я НЕ ХОЧУ ЭТО ПРОДОЛЖАТЬ!!!
# КАКАЯ РАЗНИЦА, ЧТО НЕТ ЭФФЕКТИВНОСТИ! ЕСЛИ РАБОТАЕТ, ТО ПРОДОЛЖАЕМ!!!
