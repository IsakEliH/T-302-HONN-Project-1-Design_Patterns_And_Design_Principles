from structured_logging.command_queue import Queue
from structured_logging.configuration import LoggerConfig
from injector import Module, provider, singleton
from structured_logging.logger.logger import Logger


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config

    @provider
    @singleton
    def provide_logger(self) -> Logger:
        queue = Queue(self.__logger_config.async_wait_delay_in_seconds)
        logger = Logger(self.__logger_config, queue)
        return logger
