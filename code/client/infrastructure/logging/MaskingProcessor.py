from abc import ABC, abstractmethod


class MaskingProcessor():
    def __init__(self, list_keys: list, main_dict: dict):
        self.list_keys = list_keys
        self.main_dict = main_dict

    @abstractmethod
    def change_keys(self, list_key: list, main_dict: dict):
        for i in list_key:
            if i == main_dict:
                main_dict[i] = "***"