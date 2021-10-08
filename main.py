import sqlite3
from datetime import datetime

# текущие дата и время
current_date = datetime.now().date()
current_time = str(datetime.now().time().hour) + ':' + str(datetime.now().time().minute)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


def insert_into_db(row, spaces_count):
    global current_date, current_time
    for i in range(spaces_count):
        print('Parking space -', i + 1)
        brand, color = input().split()
        values = (row, i + 1, brand, color, current_date, current_time)
        cursor.execute('INSERT INTO parking_space VALUES (?, ?, ?, ?, ?, ?)', values)
        conn.commit()

# cursor.execute("""CREATE TABLE parking_space
#                 (row integer, col integer, brand text, color text, date text, time text)
#                """)


print('Текущая дата:', current_date, ', время:', current_time)

# начальные значения количества рядов на парковке [19, 10, 17]
#print('Запись первого ряда.')
#insert_into_db(1, 1)
print('Запись второго ряда.')
insert_into_db(2, 2)
#print('Запись третьего ряда..')
#insert_into_db(3, 3)
