num = int(input(f"Player please enter an integer: "))
if num >= 1 and num % 3 == 0 and num % 5:
    print(f"The input number is {num}, FuzzBuzz")
elif num >= 1 and num % 3 == 0:
    print(f"The input num is {num}, Fuzz")
elif num >= 1 and num % 5 == 0:
    print(f"The input num is {num}, Buzz")
elif num < 0:
    print("invalid entry")
else:
    print("invalid entry")