from structured_logging.command_queue import Command

class LoggingCommand(Command):
    def __init__(self, sink, data):
        self.__sink = sink
        self.__data = data

    def execute(self):
        self.__sink.sink_data(self.__data)

