import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Institute Information
# ==========================================

INSTITUTE_NAME = "Prime Computers"

WELCOME_MESSAGE = (
    "Welcome to Prime Computers. "
    "I am your AI Admission Counsellor."
)

# ==========================================
# Google Sheets
# ==========================================

SPREADSHEET_ID = "1GSwPPEmCiuzHe0aBJmYpUpbaVzVcXKEtlzQyL5WtFlY"

COURSES_SHEET = "Courses"
FAQ_SHEET = "FAQs"
LEADS_SHEET = "Leads"

# ==========================================
# AI
# ==========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-2.5-flash"

TEMPERATURE = 0.3

# ==========================================
# Contact Information
# ==========================================

PHONE = "9820016724"

WEBSITE = "https://primecomputer.co.in"