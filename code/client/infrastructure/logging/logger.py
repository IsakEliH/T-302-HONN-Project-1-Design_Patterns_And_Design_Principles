from client.infrastructure.logging.i_logger import ILogger
from structured_logging.logger.logger import Logger


class ClientLogger(ILogger):
    def __init__(self, logger: Logger):
        self.__logger = logger

    def error(self, message: str, exception: Exception = None):
        self.__logger.log(
            message=message, level="error", error=str(exception) if exception else None
        )

    def warning(self, message: str, exception: Exception = None):
        self.__logger.log(
            message=message,
            level="warning",
            warning=str(exception) if exception else None,
        )

    def info(self, message: str, object: object = None):
        self.__logger.log(message=message, level="info", object=object)
