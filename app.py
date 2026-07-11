from models.lead import Lead
from lead.lead_manager import LeadManager


lead = Lead(
    name="Aarya Khanvilkar",
    mobile="9820086724",
    email="ark@gmail.com",
    course="AI",
    message="Interested in AI course"
)

manager = LeadManager()

success, message = manager.save(lead)

print(success)
print(message)