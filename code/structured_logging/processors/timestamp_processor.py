from datetime import datetime
from structured_logging.processors.abstract_processor import AbstractProcessor



class TimestampProcessor(AbstractProcessor):
    def _before_processing(self, data):
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data["timestamp"] = time


