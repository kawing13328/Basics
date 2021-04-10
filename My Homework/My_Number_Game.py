# This is the Number Game Trial.
print("Welcome to the Number Game!")
name = input(f"Please input your name: ")
print(f"\nOK, let's start, {name}!")
answer_num = 36
count = 0
num = int(input(f"Please input a number from 1 to 50:  "))
while num != answer_num:
    if 0 < num < answer_num:
        count = count + 1
        print(f"This is the {count} times you have tried.")
        print("Your number should be bigger.")
        num = int(input(f"Please input a number from {num} to 50:  "))
    elif num > answer_num and num < 50:
        count = count + 1
        print(f"This is the {count} times you have tried.")
        print(f"Your number should be smaller.")
        num = int(input(f"Please input a number from 1 to {num}:  "))
    else:
        count = count + 1
        print(f"This is the {count} times you have tried.")
        print("This is NOT a correct entry. Please re-enter." )
        num = int(input(f"Please input a number from 1 to 50:  "))
count = count + 1
print(f"Congratulations, this is correct,{name}.")
print(f"The total times you try:{count} ")