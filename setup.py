from telegram import CallbackQuery, Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler
from data import insert_into_db, create_table_if_not_exists
import settings as settings
from my_log import logger
from app import ask_msg_amount, send_giga_answer, button


bot = Bot(token=settings.bot_token)


def main():
    create_table_if_not_exists()
    application = Application.builder().bot(bot).build()
    application.add_handler(MessageHandler(callback=insert_into_db, filters=filters.TEXT), group=0)
    application.add_handler(CommandHandler(callback=ask_msg_amount, command="summery"), group=1)
    application.add_handler(CallbackQueryHandler(button))
    logger.info("bot.starting")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("Exited")
