from datetime import datetime, time, date

from backend.models.base_model import BaseModel


class Log(BaseModel):
    __tablename__ = 'logfile'

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

    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, value: str):
        self.__activity = value

    @property
    def domain_activity(self) -> str:
        return self.__domain_activity

    @domain_activity.setter
    def domain_activity(self, value: str):
        self.__domain_activity = value

    @property
    def date_activity(self) -> date:
        return self.__date_activity

    @date_activity.setter
    def date_activity(self, value: date):
        self.__date_activity = value

    @property
    def time_activity(self) -> time:
        return self.__time_activity

    @time_activity.setter
    def time_activity(self, value: time):
        self.__time_activity = value
