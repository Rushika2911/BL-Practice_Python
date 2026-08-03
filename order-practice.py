from abc import ABC,abstractmethod
from dataclasses import dataclass



# Abstract Base Class
class DiscountPolicy(ABC):

    @abstractmethod
    def apply_discount(self, order_total: float) -> float:
        pass


class NoDiscount(DiscountPolicy):

    def apply_discount(self, amount: float) -> float:
        return amount


class PercentageDiscount(DiscountPolicy):

    def __init__(self, percentage: float):
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply_discount(self, amount: float) -> float:
        return amount * (1 - self.percentage / 100)


# Product Class
class Product:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Encapsulation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Quantity: {self.quantity}"


# Order Class
class Order:

    def __init__(self, order_id: int, discount_policy: DiscountPolicy):
        self.order_id = order_id
        self.items = []
        self.discount_policy = discount_policy

    def add_item(self, product: Product):
        self.items.append(product)

    # Total before discount
    def total(self):
        total = 0
        for product in self.items:
            total += product.price * product.quantity
        return total

    # Total after discount (Polymorphism)
    def final_total(self):
        return self.discount_policy.apply_discount(self.total())

    # Number of items
    def number_of_items(self):
        count = 0
        for product in self.items:
            count += product.quantity
        return count

    # Find a particular product
    def find_product(self, name):
        for product in self.items:
            if product.name.lower() == name.lower():
                return product
        return None

    # Dunder Method
    def __len__(self):
        return len(self.items)

    # Dunder Method
    def __str__(self):
        result = f"\nOrder ID : {self.order_id}\n"
        result += "-" * 30 + "\n"

        for product in self.items:
            result += str(product) + "\n"

        result += "-" * 30 + "\n"
        result += f"Number of Product Objects : {len(self)}\n"
        result += f"Number of Items : {self.number_of_items()}\n"
        result += f"Total Amount : {self.total()}\n"
        result += f"Final Amount : {self.final_total():.2f}"

        return result


# Products
p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 1000, 2)
p3 = Product("Keyboard", 2000, 1)

# Order
order = Order(101, PercentageDiscount(10))

order.add_item(p1)
order.add_item(p2)
order.add_item(p3)

# Print Order
print(order)

# Number of Product Objects
print("\nNumber of Product Objects:", len(order))

# Find Particular Product
product = order.find_product("Mouse")

if product:
    print("\nProduct Found:")
    print(product)
else:
    print("\nProduct Not Found")