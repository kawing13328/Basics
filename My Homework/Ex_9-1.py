""" Question:
1. Make a class called Restaurant.
2. The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type.
3. Make a method called describe_restaurant() that prints
these two pieces of information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.
4. Make an instance called restaurant from your class. Print the two attributes individually, and then
call both methods.
class Restaurant():
"""

class Restaurant():
    """A class representing a restaurant. -- """    #Step 1.

    def __init__(self, name, cuisine_type):         #Step 2.
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):                  #Step 3.
        """Display a summary of the restaurant."""

        msg = f"{self.name} serves perfect {self.cuisine_type}."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""

        msg = f"{self.name} is open. Welcome!"
        print("\n" + msg)

restaurant = Restaurant('Great Wall', 'pizza')  # Step 4.assignning values to the parameters.
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()