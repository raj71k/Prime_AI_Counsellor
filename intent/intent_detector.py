from enum import Enum

class Intent(Enum):
    GREETING = "greeting"
    ADMISSION = "admission"
    GENERAL = "general"

class IntentDetector():

    def detect(self, question):

        question = question.lower().strip()

        greetings = {
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening"
        }

        if question in greetings:
            return Intent.GREETING

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

        if any(word in question for word in lead_keywords):
            return Intent.ADMISSION

        return Intent.GENERAL