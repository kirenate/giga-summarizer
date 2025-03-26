from summary_bot.data import get_from_db, get_slice_from_db, msg_list_to_string
import pytest
from gigachat import GigaChat
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import Annotated, TypedDict
from summary_bot.gch import giga


@pytest.mark.data
def test_get_from_db_ok() -> None:
    get_from_db()


@pytest.mark.data
def test_get_slice_from_db_ok() -> None:
    get_slice_from_db()


@pytest.mark.data
def test_msg_list_to_sting_ok() -> None:
    test_message = msg_list_to_string()
    # assert test_message is str      на подумоть


@pytest.mark.langgraph
def test_langgraph():

    class State(TypedDict):
        messages: Annotated[list, add_messages]

    msg = State(
        messages=[
            'messages: [{"chatid" : "348544645", "date" : "2025-03-16 16:51:23+00:00", "user" : "eKiren", "user_input" : "Напомни, как меня зовут?" }]'
        ]
    )

    graph_builder = StateGraph(State)

    def chatbot(state: State):
        return {"messages": [giga.invoke(state["messages"])]}

    def stream_graph_updates(msg: dict[str, str]):
        for event in graph.stream(msg):
            for value in event.values():
                print(value["messages"][-1].content)

    graph_builder.add_node("chatbot", chatbot)
    graph_builder.set_entry_point("chatbot")
    graph_builder.set_finish_point("chatbot")
    graph = graph_builder.compile()
    print(chatbot(msg))
