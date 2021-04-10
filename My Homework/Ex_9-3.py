"""9-3: Users
1. Make a class called User. Create two attributes called first_name and last_name,
and then 2.  create several other attributes that are typically stored in a user profile.
3. Make a method called describe_user() that prints a summary of the user’s information.
4. Make another method called greet_user() that prints a personalized greeting to the user.
5. Create several instances representing different users, and call both methods for each user."""


class User():  # step 1.
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location, age: int):
        """Initialize the user."""
        self.first_name = first_name.title()  # Step 2. (Line12 to Line 17)
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.age = age

    def describe_user(self):  # Step 3.
        """Display a summary of the user's information."""
        print("Profile as follows:")
        print(f"\n {self.first_name}  {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
        print(f" Age:{self.age}")

    def greet_user(self):  # Step 4.
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")


albert = User('albert', 'joes', 'a_joes', 'a_joes@example.com', 'brooklyn', 18)
albert.describe_user()
albert.greet_user()
bonnie = User('bonnie', 'greenman', 'bgreen', 'bgreen@example.com', '', 30)
bonnie.describe_user()
bonnie.greet_user()
