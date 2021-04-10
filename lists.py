# Lists (Array)
# creating a list:
nums = list()
evens = []

# Operations: create, access, add element, remove element, copy
num = 11
odds = [1, 3, 5, 7, 9, 457]
# index:0  1  2  3  4  5
# n ind:-6 -5 -4 -3 -2 -1
# 5 element , size of 'odds' list is 5
# What is the element on index 2?  it is 5 , because indexing starts with 0
friends = ['jackson', 'said', 'lenur', 'tyson']

# Access
first_friend = friends[0]
print(f"friends: {friends}")
print(f"first_friend: {first_friend}")
print(f"friends[0]: {friends[0].title()}")
print(f"friends[1]: {friends[1]}")
print(f"friends[2]: {friends[2]}")
print(f"friends[3]: {friends[3]}")
# print(f"friends[4]: {friends[4]}") # IndexError: list index out of range
print(
    f"friends[-1]: {friends[-1]}")  # look at the right side of your list, negative indexes starting from the last element
print(f"friends[-3]: {friends[-3]}")
print(f"odds[-3]: {odds[-3]}")

# Adding elements:
# list.append(new_element) - this adds new_element to end of the list
# list.insert(index, new_element) - this adds new_element on the indicated index, shifts all elements to right
# add a friend : Obama to a friends list
friends.append('obama')
print(f"new friends list: {friends}")
friends.insert(0, 'messi')
friends.insert(1, 'ronaldo')
print(f"new friends list after insert: {friends}")


# resetting the existing element, only existing index should be used
friends[2] = 'mark'
print(f"new friends list after reset: {friends}")
# friends[7] = 'elon'  # IndexError: list assignment index out of range
# print(f"new friends list after adding new: {friends}")
# to comment do >> ctrl + /

# Remove the elements: by value, by index
friends.remove('mark')
# removed_one1 = friends.remove('mark') - this is not valid statement, since remove() does not return anything
# print(removed_one1)
print(f"new friends list after removing 'mark': {friends}")

removed_friends = []
removed_one = friends.pop(4)  # pop() function returns (informs) what it is removing
print(removed_one)
print(f"new friends list after popping index 4: {friends}")

del friends[-1]
print(f"new friends list after del index -1: {friends}")

friends = []
print(f"new friends list after redefining: {friends}")

# Exercises: 3-3
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
print("********* Exercises: 3-3 *********************")
print(f"I would like to own a {cars[0].title()} car.")
print(f"I would like to own a {cars[1].title()} car.")
print(f"I would like to own a {cars[2].title()} car.")
print(f"I would like to own a {cars[3].title()} car.")

# 3-4. Guest List:
print("********** 3-4. Guest List: *************")
friends = ['jackson', 'said', 'lenur', 'tyson']
print(f"Hi {friends[0].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[2].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[1].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[3].title()}, I would like to invite you to family dinner tomorrow.")

# H/W: exercises 3-1, 3-2, 3-5, 3-6, 3-7
