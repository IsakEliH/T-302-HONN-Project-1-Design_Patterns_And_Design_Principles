from abc import abstractmethod

from structured_logging.processors.i_processor import IProcessor


class AbstractProcessor(IProcessor):
    def __init__(self) -> None:
        self._next_processor: IProcessor | None = None

    def set_next(self, processor: IProcessor) -> IProcessor:
        self._next_processor = processor
        return processor

    def handle(self, data) -> str:
        self._before_processing(data)
        
        if self._next_processor :
            return self._next_processor.handle(data)
        return None

    @abstractmethod
    def _before_processing(self, data):
        pass
