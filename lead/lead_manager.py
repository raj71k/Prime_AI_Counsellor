from models.lead import Lead
from database.google_sheet import GoogleSheet


class LeadManager:
    def __init__(self):

        self.db = GoogleSheet()

    def validate(self, lead: Lead):

        if not lead.name.strip():
            return False, "Name is required."

        if not lead.mobile.isdigit() or len(lead.mobile) != 10:
            return False, "Invalid mobile number."

        return True, "OK"

    def save(self, lead: Lead):
        valid, message = self.validate(lead)

        if not valid:
            return False, message

        try:

            self.db.save_lead(lead)

            return True, "Lead saved successfully."

        except Exception as e:

            return False, str(e)