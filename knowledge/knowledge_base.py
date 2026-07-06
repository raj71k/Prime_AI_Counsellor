from database.google_sheet import GoogleSheet


class KnowledgeBase:

    def __init__(self):
        self.db = GoogleSheet()

    def get_all_courses(self):
        return self.db.get_courses()

    def find_course(self, course_name):

        courses = self.get_all_courses()

        for course in courses:

            if course["Course Name"].lower() in course_name.lower():

                return course

        return None