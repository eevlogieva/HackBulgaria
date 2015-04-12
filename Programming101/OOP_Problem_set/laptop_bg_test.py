import unittest
from laptop_bg import Product, Laptop, Smartphone, Store


class ProductTest(unittest.TestCase):
    def test_init_product(self):
        new_product = Product("Lenovo", 1200, 1400)
        self.assertEqual(new_product.name, "Lenovo")
        self.assertEqual(new_product.stock_price, 1200)
        self.assertEqual(new_product.final_price, 1400)

    def test_product_profit(self):
        new_product = Product("Lenovo", 1200, 1400)
        self.assertEqual(new_product.profit(), 200)

    def test_init_laptop(self):
        new_laptop = Laptop("Lenovo", 1200, 1400, 200, 4)
        self.assertEqual(new_laptop.name, "Lenovo")
        self.assertEqual(new_laptop.stock_price, 1200)
        self.assertEqual(new_laptop.final_price, 1400)
        self.assertEqual(new_laptop.diskspace, 200)
        self.assertEqual(new_laptop.RAM, 4)

    def test_init_smartphone(self):
        new_smartphone = Smartphone("Samsung", 1000, 1200, 8.3, 43)
        self.assertEqual(new_smartphone.name, "Samsung")
        self.assertEqual(new_smartphone.stock_price, 1000)
        self.assertEqual(new_smartphone.final_price, 1200)
        self.assertEqual(new_smartphone.display_size, 8.3)
        self.assertEqual(new_smartphone.mega_pixels, 43)

    def test_init_store(self):
        new_store = Store("LaptopBG")
        self.assertEqual(new_store.name, "LaptopBG")
        self.assertEqual(new_store.products, {})

    def test_load_new_products(self):
        new_store = Store("LaptopBG")
        laptop = Laptop("Lenovo", 1200, 1400, 200, 4)
        smartphone = Smartphone("Samsung", 1000, 1200, 8.3, 43)
        new_store.load_new_products(laptop, 33)
        new_store.load_new_products(smartphone, 333)
        self.assertEqual(new_store.products, {laptop: 33, smartphone: 333})

    def test_sell_products_true(self):
        new_store = Store("LaptopBG")
        laptop = Laptop("Lenovo", 1200, 1400, 200, 4)
        new_store.load_new_products(laptop, 33)
        self.assertTrue(new_store.sell_product(laptop))
        self.assertEqual(new_store.products[laptop], 32)

    def test_sell_products_false(self):
        new_store = Store("LaptopBG")
        laptop = Laptop("Lenovo", 1200, 1400, 200, 4)
        new_store.load_new_products(laptop, 33)
        smartphone = Smartphone("Samsung", 1000, 1200, 8.3, 43)
        self.assertFalse(new_store.sell_product(smartphone))

    def test_total_income(self):
        new_store = Store("LaptopBG")
        laptop = Laptop("Lenovo", 1200, 1400, 200, 4)
        new_store.load_new_products(laptop, 33)
        self.assertEqual(new_store.total_income(), 6600)


if __name__ == '__main__':
        unittest.main()
