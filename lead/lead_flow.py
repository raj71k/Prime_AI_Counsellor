from models.lead import Lead
from lead.lead_manager import LeadManager
from constants import COURSE_NAME
from knowledge.knowledge_base import KnowledgeBase


class LeadFlow:
    def __init__(self):
        self.kb = KnowledgeBase()
    def process(self, question, memory):
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

        if not memory.lead_collection:

            if any(keyword in question_lower for keyword in lead_keywords):

                course = self.kb.find_course(question)

                if course:

                    memory.set_course(course)

                    memory.lead_collection = True
                    memory.waiting_for = "name"

                    return (
                        "Wonderful! 😊\n\n"
                        "I'd be happy to help you with admission.\n\n"
                        "May I know your name?"
                    )

        # Continue existing lead collection
        if memory.lead_collection:

            # Name
            if memory.waiting_for == "name":

                memory.student_name = question.strip()
                memory.waiting_for = "mobile"

                return (
                    f"Thank you {memory.student_name}! 😊\n\n"
                    "Please share your 10-digit mobile number."
                )

            # Mobile
            elif memory.waiting_for == "mobile":

                mobile = question.strip()

                if not mobile.isdigit() or len(mobile) != 10:
                    return "Please enter a valid 10-digit mobile number."

                memory.mobile = mobile
                memory.waiting_for = "email"

                return (
                    "Thank you! 😊\n\n"
                    "Please share your email address.\n"
                    "Or type 'skip' if you don't want to provide it."
                )

            # Email
            elif memory.waiting_for == "email":

                if question.lower().strip() == "skip":
                    memory.email = ""
                else:
                    memory.email = question.strip()

                course = memory.get_course()

                if course is None:
                    return "Sorry! Something went wrong. Please start again."

                lead = Lead(
                    name=memory.student_name,
                    mobile=memory.mobile,
                    email=memory.email,
                    course=course[COURSE_NAME],
                    message="Website enquiry"
                )

                manager = LeadManager()

                success, message = manager.save(lead)

                if success:

                    memory.clear()

                    return (
                        "🎉 Thank you!\n\n"
                        "Your enquiry has been registered successfully.\n\n"
                        "Our admission counsellor will contact you shortly."
                    )

                return message

        return None