from client.infrastructure.logging.i_logger import ILogger
from structured_logging.logger.logger import Logger


class ClientLogger(ILogger):
    def error(self, message: str, exception: Exception = None, object: object = None):
        logger = Logger()
        logger.log(message=message, level="error", error=exception, object=object)

    def warning(self, message: str, exception: Exception = None, object: object = None):
        logger = Logger()
        logger.log(message=message, level="warning", warning=exception, object=object)

    def info(self, message: str, object: object = None):
        logger = Logger()
        logger.log(message=message, level="info", object=object)
