from structured_logging.processors.abstract_processor import AbstractProcessor


class MaskingProcessor(AbstractProcessor):
    def __init__(self, list_keys: list):
        self.list_keys = list_keys

    def _before_processing(self, list_key: list, data: dict):
        for i in list_key:
            if i == data:
                data[i] = "***"