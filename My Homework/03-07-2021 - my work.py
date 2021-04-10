# 03-07-2021
# Organizing the list

# Permanent sorting
names = ['sophia', 'nicole', 'jennifer', 'rachel', 'maria', 'jane']
print(f"Before sorting: {names}")
names.sort()  # sorting in ASC order
print(f"After sorting (ASC sorting): {names}")
names.sort(reverse=True)  # sorting in DES order
print(f"After sorting (DES sorting): {names}")
print("")

# Temporarily sorting
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
sorted_cars_asc = sorted(cars)
sorted_cars_des = sorted(cars, reverse=True)
print(f"Original 'cars' list = {cars} ")
print(f"sorted_cars_asc 'cars' list = {sorted_cars_asc} ")
print(f"sorted_cars_des 'cars' list = {sorted_cars_des} ")
print("")

sorted_cars_asc_copy = sorted_cars_asc
print(f"Sorted Cars Asc = {sorted_cars_asc_copy}")
sorted_cars_asc_copy.reverse()
print(f"This is reverse of Asc sort of 'cars'\nwhich is same as Des of 'cars' = {sorted_cars_asc_copy}")
print("")

print("*****Ex3-8*****")
places = ["hawaii", "egypt", "japan", "beijing", "iceland"]
print(f"Places (original)= {places} ")
print(f"Sorted place No modification of actual = {sorted(places)}")


# Loops
for car in cars:
    print(f'I would like to own a {car.title()} car.')
