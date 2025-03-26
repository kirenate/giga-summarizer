from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from data import insert_into_db
import settings as settings
from my_log import logger
from app import send_giga_answer


bot = Bot(token=settings.bot_token)


def main():
    application = Application.builder().bot(bot).build()
    application.add_handler(MessageHandler(callback=insert_into_db, filters=filters.TEXT), group=0)
    application.add_handler(CommandHandler(callback=send_giga_answer, command="summery"), group=1)
    logger.info("bot.starting")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exited")
