import unittest
import inventory


class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = inventory.Inventory()

    def test_add_product(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        self.assertIn(1, self.inventory.products)
        self.assertEqual(100, self.inventory.products[1].stock)
        self.assertEqual(10, self.inventory.products[1].threshold)
        self.assertEqual(False, self.inventory.products[1].reorder)

    def test_product_equality(self):
        product1 = inventory.Product(1, "Product 1", 100, 10)
        product2 = inventory.Product(1, "Product 1", 100, 10)
        self.assertEqual(product1, product2)
        self.assertEqual(hash(product1), hash(product2))

    def test_add_product_already_exists(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        with self.assertRaises(ValueError):
            self.inventory.add_product(1, "Product 2", 100, 10)

    def test_add_product_invalid_id(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product(-1, "Product 1", 100, 10)

    def test_add_product_invalid_name(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product(1, "", 100, 10)

    def test_add_product_invalid_stock(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product(1, "Product 1", -1, 10)

    def test_add_product_invalid_threshold(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product(1, "Product 1", 100, 0)

    def test_update_stock_increase(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        self.inventory.update_stock(1, 10)
        self.assertEqual(110, self.inventory.products[1].stock)

    def test_update_stock_decrease(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        self.inventory.update_stock(1, -10)
        self.assertEqual(90, self.inventory.products[1].stock)

    def test_update_stock_not_found(self):
        with self.assertRaises(ValueError):
            self.inventory.update_stock(1, 10)

    def test_update_stock_invalid_stock(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        with self.assertRaises(ValueError):
            self.inventory.update_stock(1, -110)

    def test_get_stock_levels(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        stock_levels = self.inventory.get_stock_levels()
        self.assertEqual(1, len(stock_levels))

    def test_get_availability(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        self.assertEqual(True, self.inventory.get_availability(1))
        self.inventory.update_stock(1, -100)
        self.assertEqual(False, self.inventory.get_availability(1))

    def test_get_availability_not_found(self):
        with self.assertRaises(ValueError):
            self.inventory.get_availability(1)

    def test_get_reorder_products(self):
        self.inventory.add_product(1, "Product 1", 100, 10)
        self.inventory.add_product(2, "Product 2", 100, 10)
        self.inventory.update_stock(1, -95)
        reorder_products = self.inventory.get_reorder_products()
        self.assertEqual(1, len(reorder_products))
        self.assertEqual(True, next(iter(reorder_products)).reorder)


if __name__ == '__main__':
    unittest.main()
