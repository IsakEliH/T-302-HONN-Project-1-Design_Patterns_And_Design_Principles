from injector import inject

from client.infrastructure.logging.i_logger import ILogger
from structured_logging.logger.logger import Logger


class ClientLogger(ILogger):
    @inject
    def __init__(self, logger: Logger):
        self.__logger = logger
    
    def error(self, message: str, exception: Exception = None):
        self.__logger = Logger()
        self.__logger.log(message=message, level="error", error=exception)

    def warning(self, message: str, exception: Exception = None):
        self.__logger = Logger()
        self.__logger.log(message=message, level="warning", warning=exception)

    def info(self, message: str, object: object = None):
        self.__logger = Logger()
        self.__logger.log(message=message, level="info", object=object)
