import sqlite3


with sqlite3.connect("messages2.db") as connection:
    cur = connection.cursor()

    messages2 = cur.execute(
         """
         CREATE TABLE IF NOT EXISTS messages2(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         chatid TEXT NOT NULL,
         date TEXT NOT NULL,
         user TEXT NOT NULL,
         text TEXT NOT NULL
         )
    """
    )
connection.commit()
connection.close()
