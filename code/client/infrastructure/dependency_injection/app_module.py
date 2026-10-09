from logging import Logger

from infrastructure.logging import ILogger
from injector import Binder, Module
from services import IPaymentService, PaymentServiceStub
from settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    def configure(self, binder: Binder) -> None:
        # Always use the settings given
        binder.bind(Settings, to=self.__settings)

        # Bind the interfaces to the concrete classes
        binder.bind(IPaymentService, to=PaymentServiceStub)
        binder.bind(ILogger, to=Logger)
