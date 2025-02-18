#Task 1 - Variables: Your First Python Intro ##########################################################################

name = 'Rahil'
age = 26
height = 5.8

print("Task 1")
print(f"Hello, My name is {name}! I'm {age} years old and {height} feet tall")

# Task 2 - Operators: Playing with Numbers ##########################################################################

# Let's pick some numbers to work with!
num1 = 10  # First number, the big guy!
num2 = 3   # Second number, a bit smaller but still powerful!

print("\nTask 2")
# Addition
print(f"The sum of {num1} and {num2} is", num1 + num2)  # Adding num1 and num2 together

# Subtraction
print(f"The difference between {num1} and {num2} is", num1 - num2)  # Subtracting num2 from num1

# Multiplication
print(f"The product of {num1} and {num2} is", num1 * num2)  # Multiplying num1 and num2

# Division
print(f"The division of {num1} by {num2} is", round(num1 / num2, 2))  # Dividing num1 by num2 (watch out for zero division!)

# Now that we've done all these operations, I think we deserve a treat. Maybe a snack? 🍕

#Task 3 - Conditional Statements: The Number Checker ##########################################################################
print("\nTask 3")
number = int(input("Please enter a Number: "))

if number > 0:
    print("This number is positive. Awesome!")
elif number < 0:
    print("This number is negative. Better luck next time!")
elif number == 0:
    print("Zero it is. A perfect balance!")