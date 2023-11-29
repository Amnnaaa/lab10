class Person:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__address = ""

    def set_name(self, x):
        self.name = x

    def get_name(self):
        return self.name

    def set_age(self, x):
        self.age = x

    def get_age(self):
        return self.age

    def set_address(self, x):
        self.address = x

    def get_address(self):
        return self.address
     
ab = Person()
ab.set_name("amna")
ab.set_age(22)
ab.set_address("karachi")
print(ab.get_name())
print(ab.get_age())
print(ab.get_address())
