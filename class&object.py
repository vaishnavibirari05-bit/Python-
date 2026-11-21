class ShoppingCart:

    def set_details(self):
        self.name = input("Enter customer name: ")
        self.product = input("Enter product name: ")
        self.price = int(input("Enter price: "))
        self.quantity = int(input("Enter quantity: "))

    def calculate_total(self):
        self.total = self.price * self.quantity

    def apply_discount(self):
        if self.total > 45000:
            self.total = self.total * 0.90

s1=ShoppingCart()
s1.set_details()
s1.calculate_total()
s1.apply_discount()