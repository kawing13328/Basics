# 03/06/2021

print("Ex 2-1. Simple Message: Store a message in a variable, and then print that message.")
msg = 'Today, we are discussing Python.'
print(f"msg = {msg}\n")

print("Ex 2-2. Simple Messages: Store a message in a variable, and print that message.")
print("Then change the value of your variable to a new message, and print the new message.\n")
print(f"msg = {msg}\n")
msg = 'Now, I change my msg.'
print(f"New msg = {msg}\n")

# 2-3. Personal Message: Store a person’s name in a variable, and print a message to that person.
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name = 'kawing'
print("Ex 2-3")
print(f"Hello {name}, would you like to learn some Python today?\n")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
print("Ex 2-4")
print(f"name lower = {name.lower()},\nname upper = {name.upper()},\nname title = {name.title()}\n")

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author.
# Your output should look something like the following, including the quotation marks:
#   Albert Einstein once said, “A person who never made a
#   mistake never tried anything new.”
quote = f'\t\t\tAlbert Einstein once said, “A person who never made a\n\t\t\tmistake never tried anything new.”'
print("Ex 2-5")
print(quote)

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person.
# Then compose your message and store it in a new variable called message. Print your message.

print("Ex 2-6")
author = "Albert Einstein"
quote = f'\t\t\t{author} once said, “A person who never made a \n\t\t\tmistake never tried anything new.”'
print(quote)

# 2-7. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions_pkg, lstrip(),rstrip(), and strip().
personname = '\t\t\tkawing leung\t\t\t\n!!!'
print("Ex 2-7")
print(f"personname_original = {personname}")
print(f"personname_leftstrip = {personname.lstrip()}")
print(f"personname_rightstrip = {personname.rstrip()}")
print(f"personname_allstrip = {personname.strip()}")

# 2-8. Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8.
# Be sure to enclose your operations in print statements to see the results. You should create four lines that look like this:
# print(5 + 3)

print("Ex 2-8")
print(f"2+6 = {int(2 + 6)}")
print(f"16-8 = {int(16 - 8)}")
print(f"2*4 = {int(2 * 4)}")
print(f"16/2 = {int(16 / 2)}")
print("")
# 2-9. Favorite Number: Store your favorite number in a variable.
# Then, using that variable, create a message that reveals your favorite number. Print that message
luckynum = 2
print("Ex 2-9")
print(f"My favourate lucky number is : {luckynum}")
print("")

# 3-1. Names: Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.
print("Ex 3-1 -- Only names, 3-2 -- with msg to introduce??")
names = ['amy', 'bobby', 'carol', 'david', 'emily']
print(f"All friends {names}")
print(f"1st friend = {names[0].title()}")
print(f"2nd friend = {names[1].title()}")
print(f"3rd friend = {names[2].title()}")
print(f"4th friend = {names[3].title()}")
print(f"5th friend = {names[4].title()}")
print("")
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
# print a message to them. The text of each message should be the same,
# but each message should be personalized with the person’s name.
print("Ex 3-2")

# Exercises: 3-3
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
print("********* Exercises: 3-3 *********************")
print(f"I would like to own a {cars[0].title()} car.")
print(f"I would like to own a {cars[1].title()} car.")
print(f"I would like to own a {cars[2].title()} car.")
print(f"I would like to own a {cars[3].title()} car.")

# 3-4. Guest List:
print("********** 3-4. Guest List: *************")
friends = ['Amy', 'Bobby', 'Carol', 'David', 'Emily','Frank']
print(f"Hi {friends[0].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[2].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[1].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[3].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[4].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[5].title()}, I would like to invite you to family dinner tomorrow.")
print("")

print("H/W: exercises 3-1, 3-2, 3-5, 3-6, 3-7")
removed_guests = []
removed_guests.append(friends.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
print(removed_guests)
removed_guests.append(friends.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
print(removed_guests)
removed_guests.append(friends.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
print(removed_guests)
removed_guests.append(friends.pop(0))
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.\n")
print('Sorry to these guests that I cannot invite')
print(removed_guests)
print('Now my updated invitation list is: ')
print(friends)

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print statement at the end of your program
# stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print("\nEx 3-5a")

print(f"{friends[0]} can attend to my party tomorrow.")
print(f"{friends[1]} CANNOT attend to my party tomorrow.")
removed_guests.append(friends.pop(1))
print(removed_guests[-1].title() + ", I know you are not able to attend my party.")
print(removed_guests)
print(removed_guests[0] + ", please come to my party.")
friends.append(removed_guests[0])
print(f"Now, I have these guests to join my party:  {friends}")
# 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to
# the end of your program informing people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.
