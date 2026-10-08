from injector import Injector

from configuration import LoggerConfig
from infrastructure import AppModule
from logger.logger import Logger

def create_logger(logger_config: LoggerConfig) -> Logger:
    injector = Injector(AppModule(logger_config))
    return injector.get(Logger)
