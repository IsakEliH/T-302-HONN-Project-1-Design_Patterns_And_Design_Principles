from injector import Binder, Module

from client.infrastructure.logging.i_logger import ILogger
from client.infrastructure.logging.logger import ClientLogger
from client.infrastructure.logging.logger_config_factory import create_logger_config
from client.infrastructure.settings import Settings
from client.services import IPaymentService, PaymentServiceStub
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from structured_logging.logger_creation.logger_factory import create_logger


class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    def configure(self, binder: Binder) -> None:
        # Always use the settings given
        binder.bind(Settings, to=self.__settings)

        # Bind the interfaces to the concrete classes
        binder.bind(IPaymentService, to=PaymentServiceStub)

        # Create the structured logging configuration
        logger_config = create_logger_config(
            self.__settings,
            LoggerConfigBuilder(),
        )

        # Get Logger from the structured logging injector
        structured_logger = create_logger(logger_config)

        # Bind ILogger to the configured ClientLogger
        binder.bind(ILogger, to=ClientLogger(structured_logger))
