import os
import sys

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from src.memory_bank.memory_bank import MemoryBank

from dotenv import load_dotenv
load_dotenv()

memory_bank = MemoryBank()
memory_1 = memory_bank.create_memory()
memory_2 = memory_bank.create_memory()
llm = ChatAnthropic(
    model="claude-3-opus-20240229",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You're an assistant who's good at {ability}. Respond in 20 words or fewer",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)
runnable = prompt | llm
with_message_history = RunnableWithMessageHistory(
    runnable,
    lambda memory: memory_bank.get_memory(memory),
    input_messages_key="input",
    history_messages_key="history",
)
memory_1_response = with_message_history.invoke(
    {"ability": "math", "input": "What's the cosinein of a angle"},
    config=memory_1.activate_memory(),
)
memory_2_response = with_message_history.invoke(
    {"ability": "math", "input": "What's? "}, config=memory_2.activate_memory()
)
print(memory_1_response)
print(memory_2_response)
