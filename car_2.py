# using different instances to print different results
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price < 10000:
            self.tax = .12
        else:
            self.tax = .15
    def display_all(self):
        print "Price", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
        return self
car1 = Car(2000, '35mpg', "Full", "15mpg")
car2 = Car(2000, "50mph", "Not Full", "105mpg")
car3 = Car(100000, "5mph", "Not Full", "105mpg")
car4 = Car(8000, "10mph", "Not Full", "10mpg")
car5 = Car(10, "25mph", "Full", "20mpg")
car6 = Car(50000, "5mph", "Not Full", "40mpg")
car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()