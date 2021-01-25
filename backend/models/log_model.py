from datetime import datetime
from backend.models.base_model import BaseModel
from sqlalchemy import Column, String, Date, DateTime

class Log(BaseModel):
    __tablename__ = 'logfile'

    domain_activity = Column(String(length=500))
    activity = Column(String(length=500))
    time_activity = Column(DateTime(timezone=True))
    date_activity = Column(Date())

    def __init__(self, activity: str, domain_activity: str, id: int = None, date_activity: str = None,
                 time_activity: str = None):
        super().__init__(id)
        self.__activity = activity
        self.__domain_activity = domain_activity
        self.__date_activity = date_activity
        self.__time_activity = time_activity

        if date_activity is None:
            self.__date_activity = datetime.now().date()
        if time_activity is None:
            self.__time_activity = datetime.now().time()
