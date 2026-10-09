from client.infrastructure.logging.masking_processor import MaskingProcessor
from client.infrastructure.settings.settings import LoggingType, Settings
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from structured_logging.processors.timestamp_processor import TimestampProcessor


def create_logger_config(
    settings: Settings, builder: LoggerConfigBuilder
) -> LoggerConfig:
    if settings.logging_type is LoggingType.CONSOLE:
        builder.with_console_sink()
    elif settings.logging_type is LoggingType.FILE:
        builder.with_file_sink(settings.logging_file_path)
    else:  # For later scalability, when a custom sink has been added
        raise NotImplementedError("Custom sink implementation needed")
        builder.with_custom_sink(...)

    if settings.logging_is_async:
        builder.as_async(settings.logging_async_delay)

    builder.add_processor(TimestampProcessor())
    builder.add_environment(settings.environment)

    builder.add_processor(MaskingProcessor(["card_number", "security_code"]))

    return builder.build()
