from telegram import Update, Message
from telegram.ext import ContextTypes
from gch import get_giga_answer
from data import get_from_db, msg_list_to_string
from my_log import logger


async def send_giga_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("in app.py func send_giga_answer was triggered")
    assert update.effective_message and update.message is not None
    input = msg_list_to_string()
    gans = get_giga_answer(input)
    logger.info(print(gans))
    await update.message.reply_text(str(gans))


"""def stream_to_graph():
    while True:
        try:
            msg = get_from_db()
            stream_graph_updates(msg)
        except:
            ..."""
