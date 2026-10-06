from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.i_processor import IProcessor
from structured_logging.sinks.i_sink import ISink


class LoggerConfigBuilder:
    def __init__(
        self,
        sink=None,
        processor=None,
        is_async: bool = False,
        async_wait_delay_in_seconds: int = 0,
    ) -> None:
        
        if sink is None:
            self.sink: ISink = ConsoleSink()
        else:
            self.sink: ISink = sink

        if processor is None:
            self.processor: IProcessor = NullProcessor()
        else:
            self.processor: IProcessor = processor

        self.is_async: bool = is_async
        self.async_wait_delay_in_seconds: int = async_wait_delay_in_seconds

    def with_custom_sink(self, sink: ISink) -> "LoggerConfigBuilder":
        raise NotImplementedError()

    def with_file_sink(self, file_path: str) -> "LoggerConfigBuilder":
        raise NotImplementedError()

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
        raise NotImplementedError()
