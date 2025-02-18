# Step 1: Ask the User’s Age with Validation
while True:
    try:
        age = int(input("How old are you? "))  # Convert input to an integer
        
        if age < 0:  # Check for negative age
            print("Oops! Age can't be negative. Please enter a valid age.")
        else:
            break  # Valid age, exit the loop

    except ValueError:  # Handle non-numeric input
        print("Invalid input! Please enter a number.")

# Step 2: Decide the Eligibility
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference! 🎉")
else:
    years_left = 18 - age  # Calculate the years left until eligibility
    print(f"Oops! You’re not eligible yet. But hey, only {years_left} more years to go! 😊")
