from injector import inject
from client.repositories.order_repository import OrderRepository

from client.infrastructure.logging.i_logger import ILogger
from client.models.order import Order
from client.services import IPaymentService


class OrderService:
    @inject
    def __init__(
        self,
        payment_service: IPaymentService,
        order_repository: OrderRepository,
        logger: ILogger,
    ):  # order_repository was originally payment_service: PaymentServiceStub
        self.__payment_service = payment_service
        self.__logger = logger
        self.__order_repository = order_repository

    def place_order(self, order: Order):
        self.__logger.info("Order started")

        self.__payment_service.pay(order.payment)
        self.__order_repository.save(order)

        self.__logger.info("Order finished")
