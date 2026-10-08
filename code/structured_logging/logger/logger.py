from typing import Any, Iterable

from command_queue import Queue
from configuration import LoggerConfig
from logger.logging_command import LoggingCommand


class Logger:
    def __init__(self, logger_config: LoggerConfig, logging_queue: Queue):
        self.__logger_config = logger_config
        self.__logging_queue = logging_queue

    def log(self, **kwargs: Iterable[Any]):
        # 1. Runs the processing pipeline based on the given processor
        self.__logger_config.processor.handle(kwargs)
        # 2. Creates a LoggingCommand
        loggingCommand = LoggingCommand(self.__logger_config.sink, kwargs)
        # 3. if is_async is true, it adds it to the queue,
        #    otherwise the Logger object itself runs the command
        if self.__logger_config.is_async:
            self.__logging_queue.add(loggingCommand)
            return
        loggingCommand.execute()
