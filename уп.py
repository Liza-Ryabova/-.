import sqlite3
from datetime import datetime

# Создаем базу данных
conn = sqlite3.connect('support_tickets.db')
cursor = conn.cursor()

# Создаем таблицу Заявки
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Заявки (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        контактные_данные TEXT,
        описание_проблемы TEXT,
        статус TEXT
    )
''')

# Создаем таблицу Решения
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Решения (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_заявки INTEGER,
        описание_решения TEXT,
        дата_решения DATE
    )
''')

# Добавляем тестовые данные
cursor.execute('''
    INSERT INTO Заявки (контактные_данные, описание_проблемы, статус)
    VALUES ('Иванов Иван Иванович', 'Проблема с отчетом по продажам', 'закрыта')
''')
cursor.execute('''
    INSERT INTO Решения (id_заявки, описание_решения, дата_решения)
    VALUES (1, 'Проблема с отчетом по продажам', '2023-10-01')
''')

# Операции с базой данных
def get_open_tickets():
    cursor.execute("SELECT * FROM Заявки WHERE статус='открыта'")
    return cursor.fetchall()

def get_closed_tickets():
    cursor.execute("SELECT * FROM Заявки WHERE статус='закрыта'")
    return cursor.fetchall()

def get_total_tickets():
    cursor.execute("SELECT COUNT(*) FROM Заявки")
    return cursor.fetchone()[0]

def get_sorted_tickets():
    cursor.execute("SELECT * FROM Заявки ORDER BY id")
    return cursor.fetchall()

# Тестирование функций
print("Открытые заявки:")
print(get_open_tickets())

print("\nЗакрытые заявки:")
print(get_closed_tickets())

print("\nОбщее количество заявок:")
print(get_total_tickets())

print("\nЗаявки отсортированные по дате создания:")
print(get_sorted_tickets())