class Product:
    def __init__(self, product_id, name, stock, threshold):
        if product_id < 0:
            raise ValueError("Product ID should be greater than zero")
        if not name:
            raise ValueError("Invalid name")
        if stock < 0:
            raise ValueError("Stock should be greater or equal to zero")
        if threshold <= 0:
            raise ValueError("Threshold should be greater than zero")
        self.product_id = product_id
        self.name = name
        self.stock = stock
        self.threshold = threshold
        self.reorder = False

    def check_stock(self):
        return self.stock

    def is_available(self):
        return self.stock > 0

    def update_stock(self, value):
        if (self.stock + value) < 0:
            raise ValueError("Stock should be greater than zero")
        self.stock += value

    def set_reorder(self, reorder):
        self.reorder = reorder

    def __repr__(self):
        return f"{self.product_id} - {self.name}: {self.stock}"


class Inventory:
    def __init__(self):
        self.products = {}
        self.reorder_products = set()

    def add_product(self, product_id, name, stock, threshold):
        if product_id in self.products:
            raise ValueError("Product with this ID already exists")
        self.products[product_id] = Product(product_id, name, stock, threshold)

    def update_stock(self, product_id, value):
        self._validate_product(product_id)
        product = self.products[product_id]
        product.update_stock(value)
        product.set_reorder(product.stock < product.threshold)
        if product in self.reorder_products and not product.reorder:
            self.reorder_products.remove(product)
        if product not in self.reorder_products and product.reorder:
            self.reorder_products.add(product)

    def check_stock(self, product_id):
        self._validate_product(product_id)
        return self.products[product_id].stock

    def get_stock_levels(self):
        return self.products

    def get_availability(self, product_id):
        self._validate_product(product_id)
        return self.products[product_id].is_available()

    def get_reorder_products(self):
        return self.reorder_products

    def _validate_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product not found")
