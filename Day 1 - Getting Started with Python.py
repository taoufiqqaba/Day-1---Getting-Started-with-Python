import os
os.system('cls' if os.name == 'nt' else 'clear')

Day 1

print(type("Hello"))
print(type(12345))
print(type(23.44))
print(type(False))

name = input("Type Your Name Here: " )
length = len(name)
print(type("The Number of the Letters in Your Name is:")) 
print(type(length))

print("The Number of the Letters in Your Name is: " + str(length))

print("Choose a Number: ")
number1 = input()

print("Choose Another Number: ")
number2 = input()

Summary = int(number1) + int(number2)
print("The Result is: " , Summary)



