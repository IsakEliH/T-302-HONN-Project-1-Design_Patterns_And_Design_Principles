from structured_logging.processors.abstract_processor import AbstractProcessor
from structured_logging.configuration.environment import Environment


# Adds an environment to the data
class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, env: Environment):
        super().__init__()
        self._env = env

    def _before_processing(self, data):
        data["environment"] = self._env.value
