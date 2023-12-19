class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                break
        else:
            self.items.append({"product": product, "quantity": quantity})

    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.items:
                print(f"{item['product']} - Quantity: {item['quantity']}")

    def calculate_total(self):
        total_cost = sum(item["product"].price * item["quantity"] for item in self.items)
        return total_cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_product(product, quantity)

    def view_cart(self):
        self.shopping_cart.display_cart()

    def checkout(self):
        total_cost = self.shopping_cart.calculate_total()
        print(f"Total cost for {self.name}'s order: ${total_cost:.2f}")


# Example usage:

# Create products
product1 = Product("Laptop", 1200.50)
product2 = Product("Mouse", 25.99)
product3 = Product("Headphones", 99.95)

# Create a customer
customer = Customer("Alice")

# Add products to the customer's shopping cart
customer.add_to_cart(product1, 2)
customer.add_to_cart(product2, 1)
customer.add_to_cart(product3, 3)

# Display the cart contents
customer.view_cart()

# Calculate and display the total cost
customer.checkout()
