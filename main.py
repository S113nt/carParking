import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


def insert_into_db(row, spaces_count):
    global date, time
    print('Введите марку и цвет автомобиля (ч/з пробел):')
    for i in range(spaces_count):
        print('Parking space -', i + 1)
        brand, color = input().split()
        values = (row, i + 1, brand, color, date, time)
        cursor.execute('INSERT INTO parking_space VALUES (?, ?, ?, ?, ?, ?)', values)
        conn.commit()

# cursor.execute("""CREATE TABLE parking_space
#                 (row integer, col integer, brand text, color text, date text, time text)
#                """)


print('Введите текущюю дату и время.')
print('Дата в формате DD-MM-YYYY')
date = str(input())

print('Время в формате HH:MM')
time = str(input())

# Начальные значения количества рядов на парковке [19, 10, 17]
print('Запись первого ряда.')
insert_into_db(1, 1)
print('Запись второго ряда.')
insert_into_db(2, 2)
print('Запись третьего ряда.')
insert_into_db(3, 3)
