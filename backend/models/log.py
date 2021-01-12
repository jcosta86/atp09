class Log:
    def __init__(self, activity: str, domain_activity: str, id: int = None, date_activity: str = None,
                 time_activity: str = None):
        self.id = id
        self.activity = activity
        self.domain_activity = domain_activity
        self.date_activity = date_activity
        self.time_activity = time_activity
