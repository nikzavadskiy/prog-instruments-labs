import pytest
from src.warehouse import Warehouse, Product

class TestWarehouse:
    def setup_method(self):
        self.wh = Warehouse(tax_rate=0.1)
        self.wh.add_product(Product("Laptop", 1000.0, 1, "tech"))
        self.wh.add_product(Product("Mouse", 50.0, 2, "tech"))

    @pytest.mark.parametrize("category, discount, expected_laptop_price", [
        ("tech", 10, 900.0),
        ("tech", 100, 0.0),
        ("food", 50, 1000.0),
        ("tech", 0, 1000.0),
    ])
    def test_bulk_discount_logic(self, category, discount, expected_laptop_price):
        self.wh.apply_bulk_discount(category, discount)
        assert self.wh.products["Laptop"].price == expected_laptop_price

    def test_tax_calculation(self):
        # (1000*1 + 50*2) = 1100. +10% = 1210
        assert self.wh.calculate_total_with_tax() == 1210.0

    def test_product_negative_price(self):
        with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
            Product("Water", -5, 1)
