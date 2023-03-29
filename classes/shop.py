
from classes.storage import Storage


class Shop(Storage):
    def __init__(self, items, capacity=20):
        self._items = items
        self._capacity = capacity

    def add(self, name, amount):
        if self.get_unique_items_count() < 5:
            if self.get_items().get(name) is not None:
                if self.get_free_space() < amount:
                    print("В магазине недостаточно места, попробуйте заказать меньше товара")
                    raise ValueError
                else:
                    self.get_items()[name] += amount
            else:
                self.get_items()[name] = amount
            print(f"Курьер везет {amount} {name} со склада в магазин\n"
                  f"Курьер доставил {amount} {name} в магазин")
        else:
            print("Нету места для еще одного товара")
            raise ValueError

    def remove(self, name, amount):
        if self.get_items().get(name) is not None:
            if self.get_items()[name] < amount:
                print("Не хватает товара в магазине, попробуйте заказать меньше")
                raise ValueError
            else:
                self.get_items()[name] -= amount
                print('Нужное количество есть в магазине\n'
                      f'Курьер забрал {amount} {name} с магазина')
        else:
            print("В магазине нет такого товара")
            raise TypeError

    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        return self._items

    def get_unique_items_count(self):
        return len(self.get_items())

    def get_info(self):
        for item, value in self.get_items().items():
            print(item, value)
