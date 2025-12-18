class Product:
    def __init__(self, name: str, price: float, quantity: int, category: str = "general"):
        if price < 0: 
            raise ValueError("Цена не может быть отрицательной")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

class Warehouse:
    def __init__(self, tax_rate: float = 0.2):
        self.products = {}
        self.tax_rate = tax_rate

    def add_product(self, product: Product):
        self.products[product.name] = product

    def apply_bulk_discount(self, category: str, discount_percent: float):
        if not (0 <= discount_percent <= 100):
            raise ValueError("Скидка должна быть от 0 до 100")
        for p in self.products.values():
            if p.category == category:
                p.price *= (1 - discount_percent / 100)

    def get_stock_report(self):
        return {name: p.quantity for name, p in self.products.items()}

    def calculate_total_with_tax(self):
        total = sum(p.price * p.quantity for p in self.products.values())
        return round(total * (1 + self.tax_rate), 2)
