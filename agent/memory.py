"""
memory.py
----------
Conversation memory.
"""


class ConversationMemory:

    def __init__(self, max_history=5):

        self.max_history = max_history

        self.history = []

    def add(self, user, assistant):

        self.history.append({"user": user, "assistant": assistant})

        if len(self.history) > self.max_history:

            self.history.pop(0)

    def get_context(self):

        context = ""

        for chat in self.history:

            context += f"""
User:
{chat["user"]}

Assistant:
{chat["assistant"]}

"""

        return context

    def clear(self):

        self.history.clear()
