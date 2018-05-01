class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def display_info(self):
        print "Price: ", self.price
        print "max speed: ", self.max_speed
        print "miles: ", self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles <= 5: 
            self.miles = 0
        else:
            self.miles -= 5
        return self
bike1 = Bike('200', '20', '0')
bike2 = Bike('100', '10', '0')
bike3 = Bike('1', '1', '0')
print bike1.ride().ride().ride().display_info()
print bike2.ride().ride().reverse().reverse().display_info()
print bike3.reverse().reverse().reverse().display_info()