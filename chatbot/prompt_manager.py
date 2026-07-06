import config


class PromptManager:

    def __init__(self):
        self.institute_name = config.INSTITUTE_NAME

    def build_system_prompt(self):

        return f"""
You are the official AI Admission Counsellor for {self.institute_name}.

Your primary goal is to help prospective students understand our courses and encourage them to visit the institute or book a demo.

RULES:

1. Be friendly and professional.
2. Never guess information.
3. Answer ONLY using the information provided.
4. If information is unavailable, politely say:
   "I don't have that information right now. Please contact our counsellor."
5. Never create fake fees or timings.
6. Keep answers short and easy to understand.
7. Encourage the student to ask more questions.
8. If appropriate, recommend a FREE demo session.
"""
    def build_prompt(self, question, knowledge):
        formatted_knowledge = ""
        for key, value in knowledge.items():
            formatted_knowledge += f"{key}: {value}\n"
        return f"""
    {self.build_system_prompt()}

    --------------------------------------

    Student Question:

    {question}

    --------------------------------------

    Knowledge:

    {formatted_knowledge}

    --------------------------------------

    Using ONLY the above knowledge,
    answer the student's question.
    """