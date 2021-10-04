import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

parking_spaces_1 = []
parking_spaces_2 = []
parking_spaces_3 = []


def filling_the_array(spaces_count, name_of_array):
    print('Введите цвет и марку автомобиля (ч/з пробел):')
    for i in range(spaces_count):
        print('Parking space -', i+1)
        row = input().split()
        for i in range(len(row)):
            row[i] = str(row[i])
        name_of_array.append(row)

# cursor.execute("""CREATE TABLE parking_space
#                 (row integer, col integer, brand text, color text, date text, time text)
#                """)


print('Введите текущюю дату и время.')
print('Дата в формате DD-MM-YYYY:')
date = str(input())

print('Время в формате HH:MM:')
time = str(input())

# Начальные значения количества рядов на парковке [19, 10, 17]
print('Запись первого ряда.')
filling_the_array(1, parking_spaces_1)
print('Запись второго ряда.')
filling_the_array(2, parking_spaces_2)
print('Запись третьего ряда.')
filling_the_array(3, parking_spaces_3)
