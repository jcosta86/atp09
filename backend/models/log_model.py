from datetime import datetime

from backend.models.base_model import BaseModel


class Log(BaseModel):
    __tablename__ = 'logfile'
    id = None
    activity = str()
    domain_activity = str()
    date_activity = str()
    time_activity = str()

    def __init__(self, activity: str, domain_activity: str, id: int = None, date_activity: str = None,
                 time_activity: str = None):
        self.id = id
        self.activity = activity
        self.domain_activity = domain_activity
        self.date_activity = date_activity
        self.time_activity = time_activity
        if date_activity is None:
            self.date_activity = datetime.now().date()
        if time_activity is None:
            self.time_activity = datetime.now().time()
