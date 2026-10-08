from processors import AbstractProcessor
from configuration import Environment



# Adds an environment to the data
class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, env: Environment):
        self._env = env
        
    def _before_processing(self, data):
        environment = self._env
        data["environment"] = environment

