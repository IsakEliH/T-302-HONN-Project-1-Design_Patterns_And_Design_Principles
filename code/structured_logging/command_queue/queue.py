import threading
from structured_logging.command_queue.command import Command

import time


class Queue:
    # TODO: we also need to inject the async async_wait_delay_in_seconds time into the constructor
    def __init__(self, async_wait_delay_in_seconds):
        self.__async_wait_delay_in_seconds = async_wait_delay_in_seconds
        self.__commands = list()
        self.__lock = threading.lock()

        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):
        with self.__lock:
            self.__commands.append(command)

    def __process(self):
        while True:
            command = None
            with self.__lock:
                if self.__commands: # If the list is not Empty
                    command = self.__commands.pop(0)

            if command is not None:
                command.execute()

            else:
                time.sleep(self.__async_wait_delay_in_seconds)