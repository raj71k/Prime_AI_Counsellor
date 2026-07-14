from knowledge.knowledge_base import KnowledgeBase
from chatbot.prompt_manager import PromptManager
from chatbot.ai_engine import AIEngine
from memory.conversation_memory import ConversationMemory

class ConversationEngine:

    def __init__(self):
        self.kb = KnowledgeBase()
        self.pm = PromptManager()
        self.ai = AIEngine()
        self.memory = ConversationMemory()

    def chat(self, question):
        # ==========================================
        # Lead Collection Flow
        # ==========================================

        if self.memory.lead_collection:

            if self.memory.waiting_for == "name":

                self.memory.student_name = question
                self.memory.waiting_for = "mobile"

                return (
                f"Thank you {question}! 😊\n\n"
                "Please share your mobile number."
             )
            
        question_lower = question.lower()

        lead_keywords = [
            "join",
            "admission",
            "interested",
            "enroll",
            "enrol",
            "register",
            "demo",
            "book demo"
        ]

        if any(keyword in question_lower for keyword in lead_keywords):

            course = self.kb.find_course(question)

        if course:
            self.memory.set_course(course)

        self.memory.lead_collection = True
        self.memory.waiting_for = "name"

        return (
            "Wonderful! 😊\n\n"
            "I'd be happy to help you with admission.\n\n"
            "May I know your name?"
        )    
        course = self.kb.find_course(question)
        if course:
            self.memory.set_course(course)
        else:

            course = self.memory.get_course()

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