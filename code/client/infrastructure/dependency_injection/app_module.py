from injector import Binder, Module, provider

from client.infrastructure.settings.settings import Settings


class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    @provider
    def configure(self, binder: Binder) -> None:
        pass