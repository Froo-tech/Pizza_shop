import sqlite3
import random
import string

pagenumber = [random.randint(0, 9) for _ in range(15)] + [random.choice(string.ascii_letters) for _ in range(15)]
random.shuffle(pagenumber)

pagenumber_str = ''.join(map(str, pagenumber))
print(f"Строка pagenumber_str: {pagenumber_str}")

bd = sqlite3.connect("mybd.db")
c = bd.cursor()

# Создание таблицы с указанием всех столбцов
c.execute("""
 CREATE TABLE IF NOT EXISTS user (
  login TEXT,
  email TEXT, # Add the email column here
  password TEXT,
  c_password TEXT,
  pagenumber TEXT
 )
""")

# Вставка данных с учетом всех столбцов
c.execute("INSERT INTO user (login, email, password, c_password, pagenumber) VALUES (?, ?, ?, ?, ?)", ('ME_AKK', 'myemail@example.com', '122', '122', pagenumber_str))

bd.commit()

c.execute("SELECT * FROM user")
rows = c.fetchall()
print(rows)

bd.close()
