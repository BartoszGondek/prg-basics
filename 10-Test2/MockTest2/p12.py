import re

# Read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# Pattern (criteria) for username and password
# Username should be at least 6 characters and only contain lowercase letters
username_pattern = r'^[a-z]{6,}$'

# Password should be at least 8 characters and contain only letters (lowercase/uppercase), numbers, and underscores
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# Check if username and password match the criteria
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# Print results
if username_match and password_match:
    print("Username and password are valid.")
else:
    print("Invalid username or password.")
