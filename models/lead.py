from dataclasses import dataclass
from datetime import datetime


@dataclass
class Lead:

    name: str
    mobile: str
    email: str
    course: str
    message: str
    source: str = "Website"
    status: str = "New"

    created_at: str = datetime.now().strftime("%d-%m-%Y %H:%M")