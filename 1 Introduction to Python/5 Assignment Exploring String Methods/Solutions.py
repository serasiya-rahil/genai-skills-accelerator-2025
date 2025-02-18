# Task 1 - String Slicing and Indexing
s = "Python is amazing!"

# Extracting parts using slicing
first_word = s[:6]  # First 6 characters
amazing_part = s[10:17]  # The word 'amazing'
reversed_string = s[::-1]  # Entire string in reverse order

# Printing results
print(f"First word: {first_word}")
print(f"Amazing part: {amazing_part}")
print(f"Reversed string: {reversed_string}")

# Task 2 - String Methods
s2 = " hello, python world! "

# Applying string methods
stripped = s2.strip()
capitalized = stripped.capitalize()
replaced = stripped.replace("world", "universe")
uppercased = stripped.upper()

# Printing results
print(f"Stripped: {stripped}")
print(f"Capitalized: {capitalized}")
print(f"Replaced: {replaced}")
print(f"Uppercased: {uppercased}")

# Task 3 - Check for Palindromes
user_input = input("Enter a word: ").strip()
reversed_input = user_input[::-1]

if user_input == reversed_input:
    print(f"Yes, '{user_input}' is a palindrome!")
else:
    print(f"No, '{user_input}' is not a palindrome.")
