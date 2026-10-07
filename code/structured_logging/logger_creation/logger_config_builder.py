from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.i_processor import IProcessor
from structured_logging.sinks.i_sink import ISink


class LoggerConfigBuilder:
    def __init__(self) -> None:
        self._clear()

    def with_custom_sink(self, sink: ISink) -> "LoggerConfigBuilder":
        raise NotImplementedError()

    def with_file_sink(self, file_path: str) -> "LoggerConfigBuilder":
        self.file_path: str = file_path
        self.sink = FileSink()
        return self

    def with_console_sink(self) -> "LoggerConfigBuilder":
        raise NotImplementedError()

    def as_async(self, wait_delay_in_seconds: int) -> "LoggerConfigBuilder":
        raise NotImplementedError()

    def add_environment(self, environment: Environment) -> "LoggerConfigBuilder":
        raise NotImplementedError()

    def add_processor(self, processor: IProcessor) -> "LoggerConfigBuilder":
        raise NotImplementedError()

    def _clear(self) -> None:
        self.sink: ISink = ConsoleSink()
        self.processor: IProcessor = NullProcessor()
        self.is_async: bool = False
        self.async_wait_delay_in_seconds: int = 0

    def build(self) -> LoggerConfig:
        if isinstance(self.sink, ConsoleSink):
            sink = self.with_console_sink()
        elif isinstance(self.sink, FileSink):
            sink = self.with_file_sink(self.file_path)
        else:
            sink = self.with_custom_sink()

        # Specify the processing work for the logging data

        # Then go through Async process
        if self.is_async:
            self.as_async(self.async_wait_delay_in_seconds)

        raise NotImplementedError()
