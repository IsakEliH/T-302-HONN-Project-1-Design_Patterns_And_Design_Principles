from abc import abstractmethod
from datetime import datetime

from structured_logging.configuration.environment import Environment
from i_processor import IProcessor

class AbstractProcessor(IProcessor):
    _next_processor: IProcessor = None

    def set_next(self, processor: IProcessor) -> IProcessor:
        self._next_processor = processor
        return processor

    @abstractmethod
    def handle(self, data) -> str:
        if self._next_processor:
            return self._next_processor.handle(data)
        return None


# does Nothing if other Processors arn't able to handle the input
class NullProcessor(IProcessor):
    def set_next(self, processor):
        pass

    def handle(self, data):
        pass

# add the current time and date to the data
# TODO might have to add an if "timestamp" in data, 
#       Then would have to likely add baseProcessor with _init_
class TimestampProcessor(AbstractProcessor):
    def handle(self, data):
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data["timestamp"] = time



# Adds an environment to the data
class EnvironmentProcessor(AbstractProcessor):
    def handle(self, data):
        environment = Environment.PRODUCTION    #TODO how do we choose the environment
        data["environment"] = environment