from i_logger import ILogger

class Logger(ILogger):
    def error(self, message: str, exception: Exception = None):
        print(message, exception)

    def warning(self, message: str, exception: Exception = None):
        print(message, exception)

    def info(self, message: str):
        print(message)