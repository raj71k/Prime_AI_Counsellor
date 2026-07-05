from database.google_sheet import GoogleSheet

db = GoogleSheet()

courses = db.get_courses()

for course in courses:

    print(course["Course Name"])