class Product():
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store():
    def __init__(self, name):
        self.name = name
        self.products = {}

    def load_new_products(self, product, count):
        self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if type(product) is product_class:
                print(product.name)

    def sell_product(self, product):
        if product not in self.products or self.products[product] == 0:
            return False
        else:
            self.products[product] -= 1
            return True

    def total_income(self):
        total = 0
        for product in self.products:
            total += product.profit() * self.products[product]
        return total

store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)


print(store.total_income())  # 640
