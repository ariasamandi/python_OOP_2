# creating a product class and giving attributes and methods in order to chain functions to do different functions for different instances
class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For sale"
    def sell(self):
        print "SOLD!"
        self.status = "sold"
        return self
    def add_tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self
    def return1(self, reason):
        if reason == "defective":
            self.status = "defective"
        elif reason == 'new':
            self.status = "For sale"
        elif reason == 'opened':
            self.status = "Used"
            self.price = self.price - (self.price * .2)
        return self
    def display_info(self):
        print "Price:", self.price
        print "Item name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self
product1 = Product(20, "Book", "2 pounds", "Chegg", "For sale")
product2 = Product(100, "wallet", "2 pounds", "rag n bone", "For sale")
product1.sell().add_tax(.18).display_info()
product2.return1("opened").display_info()
