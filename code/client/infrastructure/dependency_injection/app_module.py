from injector import Binder, Module
from services import IPaymentService, OrderService, PaymentServiceStub
from infrastructure.logging import ILogger
from settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    def configure(self, binder: Binder) -> None:
        pass
