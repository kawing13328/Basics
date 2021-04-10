countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barceloca']
companies = ['level up', 'abc company', 'ola company']

customers =[companies, cities, countries]
print(f"This will print all details:\n {customers}")
print("***** Print all companies only ******")
print(customers[0])
print("")
print("***** Print first company only ******")
print(customers[0][0])
print("")
print(customers[0])
print(customers[1])
print(customers[2])
print(f"Companies (barceloca) - Row 2; Column 3: {customers[1][2]}")
