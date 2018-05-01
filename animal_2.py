class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health 
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health: ", self.health
        return self
class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print "Health: ", self.health
        print "I am a Dragon"
        return self
animal1 = Animal('wolve', 150)
dog1 = Dog("pappillion", 100)
dragon1 = Dragon("fire", 500)
animal1.walk().walk().walk().run().run().display_health()
dog1.walk().walk().walk().run().run().pet().display_health()
dragon1.fly().walk().display_health()

