from datetime import datetime
from processors import AbstractProcessor



class TimestampProcessor(AbstractProcessor):
    def _before_processing(self, data):
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data["timestamp"] = time


