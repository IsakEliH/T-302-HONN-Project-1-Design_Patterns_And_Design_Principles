from structured_logging.processors.abstract_processor import AbstractProcessor



# does Nothing if other Processors arn't able to handle the input
class NullProcessor(AbstractProcessor):
    def _before_processing(self, data):
        pass