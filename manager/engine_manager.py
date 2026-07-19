from chatbot.conversation_engine import ConversationEngine


class EngineManager:

    def __init__(self):
        self.engines = {}

    def get_engine(self, user_id):

        if user_id not in self.engines:

            self.engines[user_id] = ConversationEngine()

            print(f"Created new session for {user_id}")

        return self.engines[user_id]