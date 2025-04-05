from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Message, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from gch import get_giga_answer
from data import get_from_db, msg_list_to_string, msg_list_to_string_amount
from my_log import logger


async def send_giga_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("in app.py func send_giga_answer was triggered")
    assert update.effective_message and update.message is not None
    input = msg_list_to_string()
    gans = get_giga_answer(input)
    logger.info(print(gans))
    await update.message.reply_text(str(gans))


async def ask_msg_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.message is not None
    keyboard = [
        [InlineKeyboardButton("100", callback_data="100"), InlineKeyboardButton("300", callback_data="300")],
        [InlineKeyboardButton("500", callback_data="500")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Сколько сообщений зарезюмировать?", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    assert query and query.data and update.effective_message is not None
    # logger.info(query.data)
    # logger.info(query.data[0])
    # logger.info(query.data[1])
    # logger.info(query.data[2])
    # logger.info(str(query.data[0] + query.data[1] + query.data[2]))
    amount = str(query.data[0] + query.data[1] + query.data[2])
    input = msg_list_to_string_amount(amount)
    gans = str(get_giga_answer(input))
    await query.answer(text="По последним {query.data} сообщениям вышло так...")
    await update.effective_message.reply_text(str(gans))


'''async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the inline query. This is run when you type: @botusername <query>"""
    try:
        assert update.inline_query is not None
        query = update.inline_query.query
        await send_giga_answer(update=update, context=context)
    except:
        return

'''

"""def stream_to_graph():
    while True:
        try:
            msg = get_from_db()
            stream_graph_updates(msg)
        except:
            ..."""
