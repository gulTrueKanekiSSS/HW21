from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, amount):
        pass

    @abstractmethod
    def remove(self, name, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass