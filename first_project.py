# Validate User Input Exercise

# 1. Username is no more that 12 characters
# 2. Username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")



if len(username) > 12:
    print("Username cannot exceed 12 characters")
elif not username.isalpha():
    print("Your username can't contain numbers")
elif username.find(" ") == -1:
    print("Your username can't contain spaces")
else:
    print(f"Welcome {username}")

