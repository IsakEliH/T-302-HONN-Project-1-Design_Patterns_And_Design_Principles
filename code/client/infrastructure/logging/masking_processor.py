from structured_logging.processors.abstract_processor import AbstractProcessor


class MaskingProcessor(AbstractProcessor):
    def __init__(self, list_keys: list):
        super().__init__()
        self.list_keys = list_keys

    def _before_processing(self, data: dict):
        object_data = data.get("payment")

        if not isinstance(object_data, dict):
            return

        for key in self.list_keys:
            if key in object_data:
                object_data[key] = "***"
