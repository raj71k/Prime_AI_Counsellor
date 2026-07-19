from knowledge.knowledge_base import KnowledgeBase
from chatbot.prompt_manager import PromptManager
from chatbot.ai_engine import AIEngine
from memory.conversation_memory import ConversationMemory
from models.lead import Lead
from lead.lead_manager import LeadManager
from constants import COURSE_NAME

class ConversationEngine:

    def __init__(self):
        self.kb = KnowledgeBase()
        self.pm = PromptManager()
        self.ai = AIEngine()
        self.memory = ConversationMemory()

    def chat(self, question):

    # ==========================================
    # STEP 1 : Continue Lead Collection
    # ==========================================

        if self.memory.lead_collection:

            # ---------- Collect Name ----------
            if self.memory.waiting_for == "name":

                self.memory.student_name = question.strip()
                self.memory.waiting_for = "mobile"

                return (
                    f"Thank you {self.memory.student_name}! 😊\n\n"
                    "Please share your 10-digit mobile number."
                )

            # ---------- Collect Mobile ----------
            elif self.memory.waiting_for == "mobile":

                mobile = question.strip()

                if not mobile.isdigit() or len(mobile) != 10:
                    return "Please enter a valid 10-digit mobile number."

                self.memory.mobile = mobile
                self.memory.waiting_for = "email"

                return (
                    "Thank you! 😊\n\n"
                    "Please share your email address.\n"
                    "Or type 'skip' if you don't want to provide it."
                )

            # ---------- Collect Email ----------
            elif self.memory.waiting_for == "email":

                if question.strip().lower() == "skip":
                    self.memory.email = ""
                else:
                    self.memory.email = question.strip()

                course = self.memory.get_course()

                if course is None:
                    return "Sorry! Something went wrong. Please start again."

                lead = Lead(
                    name=self.memory.student_name,
                    mobile=self.memory.mobile,
                    email=self.memory.email,
                    course=course[COURSE_NAME],
                    message="Website enquiry"
                )

                manager = LeadManager()
                success, message = manager.save(lead)

                if success:
                    self.memory.clear()

                    return (
                        "🎉 Thank you!\n\n"
                        "Your enquiry has been registered successfully.\n\n"
                        "Our admission counsellor will contact you shortly."
                    )

                return message

        # ==========================================
        # STEP 2 : Detect Admission Intent
        # ==========================================

        question_lower = question.lower()

        lead_keywords = [
            "join",
            "admission",
            "enroll",
            "enrol",
            "register",
            "interested",
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

        # ==========================================
        # STEP 3 : Normal AI Conversation
        # ==========================================

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