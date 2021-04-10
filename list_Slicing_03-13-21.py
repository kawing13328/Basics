# 03-13-2021 List_Slicing - Working with part of the list.
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']

for car in cars[1:3]:       # loop and print only index 1, 2 in cars; see the 2 is the "3" -1; "3" is NOT included.
    print(f"The car is : {car}")

print("\n********Second*******")
for car in cars [:3]:
   print(f"The car is : {car}")
