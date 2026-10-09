from structured_logging.configuration import Environment, LoggerConfig
from structured_logging.processors import (
    EnvironmentProcessor,
    IProcessor,
    NullProcessor,
)
from structured_logging.sinks import ConsoleSink, FileSink, ISink


class LoggerConfigBuilder:
    def __init__(self) -> None:
        self.sink: ISink
        self.processor: IProcessor
        self.is_async: bool
        self.async_wait_delay_in_seconds: int
        self._clear()

    def with_custom_sink(self, sink: ISink) -> "LoggerConfigBuilder":
        self.sink = sink
        return self

    def with_file_sink(self, file_path: str) -> "LoggerConfigBuilder":
        self.sink = FileSink(file_path)
        return self

    def with_console_sink(self) -> "LoggerConfigBuilder":
        self.sink = ConsoleSink()
        return self

    def as_async(self, wait_delay_in_seconds: int) -> "LoggerConfigBuilder":
        self.is_async = True
        self.async_wait_delay_in_seconds = wait_delay_in_seconds
        return self

    def add_environment(self, environment: Environment) -> "LoggerConfigBuilder":
        processor = EnvironmentProcessor(environment)
        return self.add_processor(processor)

    def add_processor(self, processor: IProcessor) -> "LoggerConfigBuilder":
        self._last_processor.set_next(processor)
        self._last_processor = processor
        return self

    def _clear(self) -> None:
        self.sink: ISink = ConsoleSink()
        self.processor: IProcessor = NullProcessor()
        self._last_processor: IProcessor = self.processor

        self.is_async: bool = False
        self.async_wait_delay_in_seconds: int = 0

    def build(self) -> LoggerConfig:
        return LoggerConfig(
            sink=self.sink,
            processor=self.processor,
            is_async=self.is_async,
            async_wait_delay_in_seconds=self.async_wait_delay_in_seconds,
        )
