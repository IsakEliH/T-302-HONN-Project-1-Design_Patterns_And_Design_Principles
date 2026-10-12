from injector import Injector

from structured_logging.configuration import LoggerConfig
from structured_logging.infrastructure import AppModule
from structured_logging.logger.logger import Logger

def create_logger(logger_config: LoggerConfig) -> Logger:
    injector = Injector(AppModule(logger_config))
    return injector.get(Logger)
