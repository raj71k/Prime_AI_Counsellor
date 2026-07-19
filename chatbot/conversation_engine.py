from knowledge.knowledge_base import KnowledgeBase
from chatbot.prompt_manager import PromptManager
from chatbot.ai_engine import AIEngine
from memory.conversation_memory import ConversationMemory
from models.lead import Lead
from lead.lead_manager import LeadManager
from constants import COURSE_NAME
from lead.lead_flow import LeadFlow
from intent.intent_detector import IntentDetector
from intent.intent_detector import Intent

class ConversationEngine:

    def __init__(self):
        self.kb = KnowledgeBase()
        self.pm = PromptManager()
        self.ai = AIEngine()
        self.memory = ConversationMemory()
        self.lead_flow = LeadFlow()
        self.intent = IntentDetector()

    def chat(self, question):
        intent = self.intent.detect(question)
    # ==========================================
    # STEP 1 : Continue Lead Collection
    # ==========================================
        if(self.memory.lead_collection or intent == Intent.ADMISSION):
            response = self.lead_flow.process(
            question,
            self.memory,
            )
            if response:
                return response

        # ==========================================
        # STEP 2 : Detect Admission Intent
        # ==========================================

        # ==========================================
        # STEP 3 : Normal AI Conversation
        # ==========================================
       
        if intent == Intent.GREETING:
            return (
                "Hello! 😊 Welcome to Prime Computers.\n\n"
                "How can I help you today?\n\n"
                "You can ask me about our courses, fees, duration, or admission."
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

        return self.ai.ask(prompt)