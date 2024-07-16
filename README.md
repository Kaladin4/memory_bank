# Memory Bank

Memory Bank is a simple Python library for managing chat message history in memory. It provides an easy way to create, store, and retrieve chat messages for different sessions.

## Installation

Straightforward installation with pipenv in case you want to try out the test cases. Be sure to install dependencies in development mode as well.

## Features

- Create unique memory sessions
- Store and retrieve chat messages
- Asynchronous support
- Clear message history
- Session-based memory management

## API Reference

### MemoryBank

- create_memory(): Creates a new Memory instance with a unique session ID.
- get_memory(session_id): Retrieves a Memory instance by session ID.

### Memory
- add_message(message): Adds a message to the memory.
- add_messages(messages): Adds multiple messages to the memory.
- clear(): Clears all messages from the memory.
- get_messages(): Returns all messages in the memory.
- get_session_id(): Returns the session ID of the memory.
- activate_memory(): Returns a dictionary with the session ID.
- Async versions of these methods are also available with the prefix a (e.g., aadd_messages, aclear, aget_messages).



