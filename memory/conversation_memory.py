class ConversationMemory:

    def __init__(self):
        self.current_course = None
        self.student_name = None
        self.mobile = None
        self.email = None
        self.lead_collection = False

        self.waiting_for = None

    def set_course(self, course):

        self.current_course = course

    def get_course(self):

        return self.current_course

    def clear(self):

        self.current_course = None
        self.student_name = None
        self.mobile = None
        self.email = None
        self.lead_collection = False

        self.waiting_for = None