from injector import Binder, Module

from client.infrastructure.logging import ILogger, Logger
from client.infrastructure.settings import Settings
from client.services import IPaymentService, PaymentServiceStub


class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    def configure(self, binder: Binder) -> None:
        # Always use the settings given
        binder.bind(Settings, to=self.__settings)

        # Bind the interfaces to the concrete classes
        binder.bind(IPaymentService, to=PaymentServiceStub)
        binder.bind(ILogger, to=Logger)
