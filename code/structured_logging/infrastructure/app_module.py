
from injector import Module, provider

from configuration import LoggerConfig
from logger.logger import Logger
from command_queue import Queue


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config

    @provider
    def provide_logger(self) -> Logger:
        queue = Queue(self.__logger_config.async_wait_delay_in_seconds)
        logger = Logger(self.__logger_config, queue)
        return logger



