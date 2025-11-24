"""
Single Responsibility Principle (SRP) – SOLID

SRP states that:
    - A class should have **only one reason to change**.
    - Each module/class/function should focus on **a single responsibility**.

When a class handles multiple concerns (e.g., business logic, formatting,
persistence, validations), any change in one concern risks breaking the others.

Below:
1) A “bad example” where one class has multiple responsibilities.
2) A refactored version applying SRP by separating concerns.
"""

class Order:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(item["price"] for item in self.items)

    # ❌ responsibility: printing + formatting (UI logic)
    def print_receipt(self):
        print("Receipt:")
        for item in self.items:
            print(f"- {item['name']}: ${item['price']}")
        print(f"Total: ${self.total()}")

    # ❌ responsibility: persistence (data storage)
    def save_to_db(self):
        print("Saving order to database...")


# Business logic only
class Order:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(item["price"] for item in self.items)


# Handles formatting/presentation
class OrderPrinter:
    def print(self, order: Order):
        print("Receipt:")
        for item in order.items:
            print(f"- {item['name']}: ${item['price']}")
        print(f"Total: ${order.total()}")


# Handles persistence/storage
class OrderRepository:
    def save(self, order: Order):
        print("Saving order to database...")
