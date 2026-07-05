from database.google_sheet import GoogleSheet
from knowledge.knowledge_base import KnowledgeBase

db = GoogleSheet()

courses = db.get_courses()

kb = KnowledgeBase()

course = kb.find_course("Power")

if course:

    print("Course Found\n")

    print(course)

else:

    print("Course Not Found")

'''for course in courses:

    print(course["Course Name"])'''