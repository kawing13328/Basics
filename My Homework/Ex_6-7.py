countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barceloca']
companies = ['level up', 'abc company', 'ola company']

customers =[companies, cities, countries]

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102). first_name, last_name, age, city they live
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.

print("***** Ex 6-7 *****")
friend1 = {'first_name': 'mathew', 'last_name': 'cheung', 'age': 38, 'city': 'toronto'} #dict1
friend2 = {'first_name': 'marcus', 'last_name': 'sujan', 'age': 40, 'city': 'hong kong'} #dict2
friend3 = {'first_name': 'robert', 'last_name': 'white', 'age': 20, 'city': 'paris'} #dict3

people = {                                                                                      #3 sub-dicts in 1 big dict
    'friend1' : {'first_name': 'mathew', 'last_name': 'cheung', 'age': 38, 'city': 'toronto'},
    'friend2' : {'first_name': 'marcus', 'last_name': 'sujan', 'age': 40, 'city': 'hong kong'},
    'friend3' : {'first_name': 'robert', 'last_name': 'white', 'age': 20, 'city': 'paris'}
        }

print(people)   # all details in people
print(friend1.keys())
for key, value in people.items():
    print(key)
    print(value)
print (people['friend1']['last_name'])

print("***** Model Answer *****")
# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'matthes',
    'age': 5,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'sitka',
}
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(f' {name}; He / She is from {city} who is {age} years old.')