from langchain_core.chat_history import BaseChatMessageHistory
from typing import List, Sequence, Any
import os
import uuid
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.messages import BaseMessage


class Memory(BaseChatMessageHistory, BaseModel):
    """In memory implementation of chat message history.

    Stores messages in an in memory list.
    """

    session_id: str = None
    messages: List[BaseMessage] = Field(default_factory=list)
    """A list of messages stored in memory."""

    def get_session_id(self):
        return self.session_id

    def activate_memory(self):
        return {"configurable": {"session_id": self.session_id}}

    async def aget_messages(self) -> List[BaseMessage]:
        """Async version of getting messages."""
        return self.messages

    def add_message(self, message: BaseMessage) -> None:
        """Add a self-created message to the store."""
        self.messages.append(message)

    async def aadd_messages(self, messages: Sequence[BaseMessage]) -> None:
        """Async add messages to the store"""
        self.add_messages(messages)

    def clear(self) -> None:
        """Clear all messages from the store."""
        self.messages = []

    async def aclear(self) -> None:
        """Async clear all messages from the store."""
        self.clear()


class MemoryBank:
    def __init__(self) -> None:
        self.memories = {}

    def create_memory(self):
        session_id = str(uuid.uuid4())
        memory = Memory(session_id=session_id)
        self.memories[session_id] = memory
        return memory

    def get_memory(self, memory_or_session_id):
        session_id = memory_or_session_id
        return self.memories[session_id]
