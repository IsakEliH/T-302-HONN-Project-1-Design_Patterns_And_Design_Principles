from pydantic import BaseSettings

from structured_logging.processors.i_processor import IProcessor
from structured_logging.sinks.i_sink import ISink
from client.infrastructure.logging.logger_config_factory import create_logger_config


class LoggerConfig(BaseSettings):
    sink: ISink
    processor: IProcessor
    is_async: bool
    async_wait_delay_in_seconds: int
    logger_config: LoggerConfig ##mitt

 # ekki viss um hvort logger_config ætti að vera fallið eða klasinn??