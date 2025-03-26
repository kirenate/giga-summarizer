from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
import settings as settings
from my_log import logger

giga = GigaChat(
    credentials=settings.credentials,
    verify_ssl_certs=False,
    scope="GIGACHAT_API_PERS",
)


def get_giga_answer(user_input: str):
    logger.info("giga triggered")
    messages = [
        SystemMessage(
            content="Ты вежливый помощник, который по запросу ОЧЕНЬ кратко описывает, что писали люди в чате до запроса"
        ),
        HumanMessage(content=user_input),
    ]
    answer = giga.invoke(messages).content
    logger.info("giga worked all funcs")
    return answer
