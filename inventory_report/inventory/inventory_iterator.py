from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self.prod = products
        self.index = 0

    def __next__(self):
        try:
            product = self.prod[self.index]

        except IndexError:
            raise StopIteration()

        else:
            self.index += 1
            return product
