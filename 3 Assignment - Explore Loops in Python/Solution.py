################################### Task 1: Counting Down with Loops ###################################
#user input for a number
number = int(input("Enter a starting number: "))

#iterate till number is greater than 0
while number > 0:
    #print the number
    print(number, end=" ")
    #subtract the number by 1 for next number to print in loop
    number-=1

#final message to print
print("Blast off! 🚀")
print()
################################## Task 2: Multiplication Table with for Loops ##################################

#user input for a table number
table_number = int(input("Enter a number: "))

#iterate in range of 1 to 10
for i in range(1,11):
    # multiply and print the number here
    print(f"{table_number} x {i} = {table_number*i}")

print()
################################## Task 3: Find the Factorial ##################################

# user to enter a number
number = int(input("Enter a number: "))

# Initialize factorial variable to 1
factorial = 1

# Use a for loop to calculate the factorial
for i in range(1, number + 1):
    factorial *= i  # Multiply factorial by the current number

# Print the result in a friendly format
print(f"The factorial of {number} is {factorial}.")
