import datetime


def process_order_system(order_data, inventory_db):
    print(f"--- Processing started at {datetime.datetime.now()} ---")

    if not order_data:
        print("Error: No order data")
        return False

    if "customer_email" not in order_data or "@" not in order_data["customer_email"]:
        print("Error: Invalid email")
        return False

    if "items" not in order_data or len(order_data["items"]) == 0:
        print("Error: Order is empty")
        return False

    for item in order_data["items"]:
        found = False
        for inv_item in inventory_db:
            if inv_item["id"] == item["id"]:
                found = True
                if inv_item["stock"] < item["quantity"]:
                    print(f"Error: Not enough stock for {item['name']}")
                    return False
        if not found:
            print(f"Error: Item {item['id']} not found in DB")
            return False

    total_price = 0
    for item in order_data["items"]:
        line_total = item["price"] * item["quantity"]

        if item.get("category") == "educational":
            line_total *= 0.85  # 15% discount
        elif item.get("category") == "electronics":
            if line_total > 500:
                line_total -= 20
            line_total *= 1.10

        total_price += line_total

    if "promo" in order_data:
        if order_data["promo"] == "SUMMER20":
            total_price *= 0.8
        elif order_data["promo"] == "FIRST_BUY":
            total_price -= 10
        elif order_data["promo"] == "VIP_MEMBER":
            if total_price > 100:
                total_price *= 0.7
            else:
                total_price *= 0.9

    if total_price < 0: total_price = 0

    print(f"Saving order for {order_data['customer_email']} to database...")

    for item in order_data["items"]:
        for inv_item in inventory_db:
            if inv_item["id"] == item["id"]:
                inv_item["stock"] -= item["quantity"]

    if order_data.get("notify_via") == "sms":
        if "phone" in order_data:
            print(f"Sending SMS to {order_data['phone']}: Order confirmed. Total: {total_price}")
        else:
            print("Error: Phone missing for SMS notification")
    else:
        print(f"Sending Email to {order_data['customer_email']}: Your order for {total_price} is ready.")

    with open("log.txt", "a") as f:
        f.write(
            f"{datetime.datetime.now()}: Processed order for {order_data['customer_email']}. Total: {total_price}\n")

    print("--- Processing finished success ---")
    return True


inventory = [
    {"id": 1, "name": "Python Book", "stock": 10},
    {"id": 2, "name": "Laptop", "stock": 2}
]

order = {
    "customer_email": "user@example.com",
    "phone": "+79991234567",
    "items": [
        {"id": 1, "name": "Python Book", "price": 100, "quantity": 2, "category": "educational"},
        {"id": 2, "name": "Laptop", "price": 1000, "quantity": 1, "category": "electronics"}
    ],
    "promo": "SUMMER20",
    "notify_via": "email"
}

process_order_system(order, inventory)
