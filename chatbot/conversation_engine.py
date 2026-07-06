from knowledge.knowledge_base import KnowledgeBase
from chatbot.prompt_manager import PromptManager
from chatbot.ai_engine import AIEngine


class ConversationEngine:

    def __init__(self):
        self.kb = KnowledgeBase()
        self.pm = PromptManager()
        self.ai = AIEngine()

    def chat(self, question):

        course = self.kb.find_course(question)

        if course is None:
            return (
                "Sorry, I couldn't find information about that course. "
                "Please try another course name."
            )

        prompt = self.pm.build_prompt(
            question=question,
            knowledge=course
        )

        answer = self.ai.ask(prompt)

        return answer