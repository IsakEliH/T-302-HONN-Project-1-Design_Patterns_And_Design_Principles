from structured_logging.processors.abstract_processor import AbstractProcessor
from structured_logging.configuration.environment import Environment



# Adds an environment to the data
class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, env: Environment):
        self._env = env
        
    def _before_processing(self, data):
        environment = self._env
        data["environment"] = environment

