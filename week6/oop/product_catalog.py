
# Creating a Product Catalog

# Instruction:

# Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.

class product():
    def __init__(self,name,price,quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"product name: {self.name}")
        print(f"product price:$ {self.price}")
        print(f"product Quantity: {self.quantity}")
        print(f"total value: $ {self.total_value()}")

product1 = product("computer",18000,3)
product2 = product("snack",18,12)

product1.display_info()
print()
print()
product2.display_info()

        


