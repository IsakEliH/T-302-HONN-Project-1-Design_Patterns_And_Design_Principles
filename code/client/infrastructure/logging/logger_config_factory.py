from client.infrastructure.settings.settings import LoggingType, Settings
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from client.infrastructure.logging.MaskingProcessor import MaskingProcessor


def create_logger_config(
    settings: Settings, builder: LoggerConfigBuilder
) -> LoggerConfig:
    if settings.logging_type is LoggingType.CONSOLE:
        builder.with_console_sink()
    elif settings.logging_type is LoggingType.FILE:
        builder.with_file_sink(settings.order_file_path)
    else:  # For later scalability, when a custom sink has been added
        raise NotImplementedError("Custom sink implementation needed")
        builder.with_custom_sink(...)

    if settings.logging_is_async:
        builder.as_async(settings.logging_async_delay)
    builder.add_environment(settings.environment)
    builder.add_processor(MaskingProcessor) ## held að maður á að gera þetta right??

    return builder.build()
