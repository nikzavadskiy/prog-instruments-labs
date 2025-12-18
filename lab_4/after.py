import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class Item:
    id: int
    name: str
    price: float
    quantity: int
    category: str

@dataclass
class Order:
    customer_email: str
    items: List[Item]
    promo: Optional[str] = None
    phone: Optional[str] = None
    notify_via: str = "email"


class OrderError(Exception): pass
class InsufficientStockError(OrderError): pass
class ValidationError(OrderError): pass


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class SummerDiscount(DiscountStrategy):
    def apply(self, total: float) -> float: return total * 0.8

class VIPDiscount(DiscountStrategy):
    def apply(self, total: float) -> float: 
        return total * 0.7 if total > 100 else total * 0.9

class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str, contact: str):
        pass

class EmailNotification(NotificationService):
    def send(self, message: str, contact: str):
        print(f"Sending Email to {contact}: {message}")

class SMSNotification(NotificationService):
    def send(self, message: str, contact: str):
        print(f"Sending SMS to {contact}: {message}")


class InventoryManager:
    def __init__(self, inventory_db: List[Dict]):
        self._db = {item["id"]: item for item in inventory_db}

    def validate_stock(self, items: List[Item]):
        for item in items:
            inv_item = self._db.get(item.id)
            if not inv_item:
                raise ValidationError(f"Item {item.id} not found")
            if inv_item["stock"] < item.quantity:
                raise InsufficientStockError(f"Not enough stock for {item.name}")

    def update_stock(self, items: List[Item]):
        for item in items:
            self._db[item.id]["stock"] -= item.quantity

class OrderValidator:
    @staticmethod
    def validate(order: Order):
        if not order.customer_email or "@" not in order.customer_email:
            raise ValidationError("Invalid email")
        if not order.items:
            raise ValidationError("Order is empty")

class PriceCalculator:
    _PROMO_MAP = {
        "SUMMER20": SummerDiscount(),
        "VIP_MEMBER": VIPDiscount()
    }

    def calculate_total(self, order: Order) -> float:
        total = sum(self._get_item_price(item) for item in order.items)
        
        if order.promo in self._PROMO_MAP:
            total = self._PROMO_MAP[order.promo].apply(total)
        elif order.promo == "FIRST_BUY":
            total -= 10
            
        return max(0, total)

    def _get_item_price(self, item: Item) -> float:
        price = item.price * item.quantity
        if item.category == "educational":
            price *= 0.85
        elif item.category == "electronics":
            if price > 500: price -= 20
            price *= 1.10
        return price


class OrderProcessor:
    def __init__(self, inventory: InventoryManager):
        self.inventory = inventory
        self.validator = OrderValidator()
        self.calculator = PriceCalculator()
        self.notifiers = {
            "email": EmailNotification(),
            "sms": SMSNotification()
        }

    def process(self, order: Order):
        print(f"--- Processing started at {datetime.datetime.now()} ---")
        try:
            self.validator.validate(order)
            self.inventory.validate_stock(order.items)
            
            total = self.calculator.calculate_total(order)
            
            self.inventory.update_stock(order.items)
            self._send_notification(order, total)
            self._log_transaction(order, total)
            
            print("--- Processing finished success ---")
            return True
        except OrderError as e:
            print(f"Order failed: {e}")
            return False

    def _send_notification(self, order: Order, total: float):
        message = f"Order confirmed. Total: {total}"
        notifier = self.notifiers.get(order.notify_via, self.notifiers["email"])
        contact = order.phone if order.notify_via == "sms" else order.customer_email
        notifier.send(message, contact)

    def _log_transaction(self, order: Order, total: float):
        with open("log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {order.customer_email} - {total}\n")
