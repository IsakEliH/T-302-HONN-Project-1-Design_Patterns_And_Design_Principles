from i_logger import ILogger
from structured_logging.logger.logger import Logger

class ClientLogger(ILogger):
    def error(self, message: str, exception: Exception = None):
        logger = Logger()
        logger.log(message=message, level="error", error=exception)

    def warning(self, message: str, exception: Exception = None):
        logger = Logger()
        logger.log(message=message, level="warning", warning=exception)

    def info(self, message: str):
        logger = Logger()
        logger.log(message=message, level="info")
