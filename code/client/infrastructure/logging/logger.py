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

## til að taka inn heilu hlutina þá meikar sense að logga objectið er það ekki?
## cuz .log tekur við kvargs svo maður ætti að geta loggað objects right?
## og handle tekur við öllum gögnum í Dict

## það er pælingin mín, Kv Viktor.
    def log_obj(self, object=object,):
        logger = Logger()
        logger.log(object=object)