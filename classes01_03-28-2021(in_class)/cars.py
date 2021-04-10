# 03/28/2021 Object-oriented Programming Concepts: Class and Object

class Car:
    """This class describes model of the car."""

    def __init__(self, brand, model, color):
        """this is the constructor, with required parameters."""
        self.brand = brand  # assigning the local brand variable to a global variable (self.brand)
        self.model = model
        self.color = color
        self.__odo_reader = 0  # encapsulation - hiding data from object(users)

    def set_odometer_reader(self, miles):
        """Function to update the value of the odo_reader global variable."""
        if miles > self.__odo_reader:
            self.__odo_reader = miles
        else:
            print("miles can not be less than odometer miles.")

    def drive(self):
        """driving action"""
        if self.brand.lower() == "bmw":
            print(f"You are driving FAST car even without DL! isn't it awesome!")
        else:
            print(f"You are driving the car even without DL! isn't it awesome!")

    def do_something(self):
        print("I want to do something .....")
        print("let me drive this car ;) ")
        self.drive()
        # motor = Motorcycle()
        # motor.drive()

    def get_description(self):
        """ """
        # print(f"Brand of the car: {self.model}") # we are using here local variable that is only inside __init__ method
        # greet_user()
        print(f"Model of the car: {self.model}")
        print(f"Color of the car: {self.color}")
        print(f"Brand of the car: {self.brand}")
        print(f"You have {self.__odo_reader} miles on your car.")


def greet_user():
    print("hello master!")


# greet_user()
# drive()
# Execution
# drive() we will not have an access to this function yet

# mycar = Car()  # Car is the class, mycar is an object, in this line we are creating instance of the (instantiation)
mycar = Car("BMW", "530xi", "black")
yourcar = Car("Lexus", "lexus IS", "silver")

print("==================================")
mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.set_odometer_reader(60)
mycar.set_odometer_reader(25)
mycar.__odo_reader = 20  # this is the direct access to the instance variables
mycar.color = 'RED'  # this is the direct access to the instance variables
mycar.get_description()
# yourcar.do_something()
print("==================================")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()
