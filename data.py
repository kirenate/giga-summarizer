import sqlite3
from telegram import Update
from telegram.ext import ContextTypes
from my_log import logger
import json


''' async def insert_into_db(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inserts all messages to messages2.db"""
    assert update.effective_message is not None

    jmessage = json.dumps(update.effective_message, ensure_ascii=False)
    connection1 = sqlite3.connect("messages2.db")
    cur1 = connection1.cursor()
    cur1.execute("INSERT INTO messages2 (json_message) VALUES (?)", (jmessage,))
    connection1.commit()
    connection1.close()

    logger.info("Message has been inserted to db") '''


async def insert_into_db(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inserts all messages to messages2.db"""
    assert update.effective_message and update.effective_chat and update.effective_sender is not None

    text = update.effective_message.text
    chatid = update.effective_chat.id
    date = update.effective_message.date
    user = update.effective_sender.username
    connection1 = sqlite3.connect("messages2.db")
    cur1 = connection1.cursor()
    cur1.execute("INSERT INTO messages2 (chatid, date, user, text) VALUES (?, ?, ?, ?)", (chatid, date, user, text))
    connection1.commit()
    connection1.close()

    logger.info("Message has been inserted to db")


def msg_list_to_string() -> str:
    msg_list_fetched = get_slice_from_db()
    msg_string = "История чата:\n\n"
    for msgs in msg_list_fetched:
        msg_string += "Друг " + msgs[2] + " пишет:\n" + msgs[3] + "\n\n\n"
    logger.info(print(msg_string))
    return msg_string


def get_slice_from_db() -> list:  # for multiple msgs
    """Gets a few of latest messages from messages2.db"""
    connection2 = sqlite3.connect("messages2.db")
    cur2 = connection2.cursor()
    cur2.execute("SELECT chatid, date, user, text FROM messages2 ORDER BY id DESC LIMIT 10")
    msg_list_fetched = cur2.fetchall()
    logger.info(print(msg_list_fetched))
    connection2.close()
    logger.info("messages2 fetched from db")
    return msg_list_fetched


def get_from_db() -> dict:  # for one msg only
    connection2 = sqlite3.connect("messages2.db")
    cur2 = connection2.cursor()
    cur2.execute("SELECT chatid, date, user, text FROM messages2 ORDER BY id DESC LIMIT 1")
    msg_fetched = cur2.fetchone()
    logger.info(print(msg_fetched))
    connection2.close()
    logger.info("Message returend from DB successfully")
    logger.info(print(msg_fetched))
    msg = {
        "messages": [
            {"chatid": msg_fetched[0], "date": msg_fetched[1], "user": msg_fetched[2], "user_input": msg_fetched[3]}
        ]
    }
    return msg


# ........................................................................................................

if __name__ == "__main__":

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
