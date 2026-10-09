from structured_logging.processors import IProcessor
from pydantic_settings import BaseSettings
from structured_logging.sinks import ISink


class LoggerConfig(BaseSettings):
    sink: ISink
    processor: IProcessor
    is_async: bool
    async_wait_delay_in_seconds: int

    class Config:
        arbitrary_types_allowed = True
