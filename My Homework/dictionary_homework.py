my_car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print("*****Ex. 6-1****** ")
my_friend = {"first_name":"Gordon","last_name":"Brown","age": 36, "city":"Brooklyn"}
print(my_friend["first_name"],my_friend["last_name"])
print("***** Concatenate ***** ")
print(f'my friend full name is: {my_friend["first_name"] + " " + my_friend["last_name"]}')
print("")
print("***** Ex. 6-5 *****")
rivers = {"nile":"egypt", "tigres":"iraq", "amazon":"brazil", "mississippi":"usa"}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
