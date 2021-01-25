from .base_dao import BaseDao
from backend.models.log_model import Log


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)
