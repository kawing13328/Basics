"""Ex 9-2: Three Restaurants
Start with your class from Exercise 9-1. Create three different instances from the class, and call
describe_restaurant() for each instance."""

class Restaurant():
    """A class representing a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves perfect {self.cuisine_type}."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

great_wall = Restaurant('great wall', 'pizza')      #object 1
great_wall.describe_restaurant()                    #call function
sakura_cuisine = Restaurant('sakura_cuisine', 'japanese food')  #object 2
sakura_cuisine.describe_restaurant()                            #call function
busy_bee = Restaurant('busy_bee', 'fast meat')      #obect 3
busy_bee.describe_restaurant()                      #call function