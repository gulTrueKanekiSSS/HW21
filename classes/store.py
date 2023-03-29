from classes.storage import Storage

class Store(Storage):
    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    def add(self, name, amount):
        if self.get_items().get(name) is not None:
            if self.get_free_space() < amount:
                print('Вы заказываете слишком много товара, закажите меньше')
                raise ValueError
            else:
                self.get_items()[name] += amount
        else:
            self.get_items()[name] = amount

    def remove(self, name, amount):
        if self.get_items().get(name) is not None:
            if self.get_free_space() < amount:
                print("Не хватает товара на складе, попробуйте заказать меньше")
                raise ValueError
            else:
                self.get_items()[name] -= amount
                print(f'Нужное количество есть на складе\n'
                      f'Курьер забрал {amount} {name} со склада')
        else:
            print("Такого товара нет на складе")
            raise TypeError

    def get_unique_items_count(self):
        return len(self.get_items())

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_info(self):
        for item, value in self.get_items().items():
            print(item, value)