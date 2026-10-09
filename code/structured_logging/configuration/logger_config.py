from pydantic import BaseModel, BaseSettings

from processors import IProcessor
from sinks import ISink


class LoggerConfig(BaseSettings):
    sink: ISink
    processor: IProcessor
    is_async: bool
    async_wait_delay_in_seconds: int

    class Config:
        arbitrary_types_allowed = True
