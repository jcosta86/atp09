import sys
sys.path.append('.')

from backend.models.log_model import Log
from backend.models.base_model import BaseModel

class TestLogModel:
    activity = "List"
    domain_activity = "Category"
    
    def test_log_model(self) -> None:
        self.log = Log(self.activity, self.domain_activity)
        assert isinstance(self.log, Log)
        assert isinstance(self.log, BaseModel)
        assert self.log.activity == self.activity
        assert self.log.domain_activity == self.domain_activity
        assert self.log.__tablename__ == 'logfile'