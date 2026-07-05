import gspread
from google.oauth2.service_account import Credentials


class GoogleSheet:

    def __init__(self):

        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_file(
            "credentials/prime-computers-ai-a866ccb58418.json",
            scopes=SCOPES
        )

        self.client = gspread.authorize(creds)

        self.spreadsheet = self.client.open_by_key("1GSwPPEmCiuzHe0aBJmYpUpbaVzVcXKEtlzQyL5WtFlY")


    def get_courses(self):

        sheet = self.spreadsheet.worksheet("Courses")

        return sheet.get_all_records()