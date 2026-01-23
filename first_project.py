# If Statements

age = int(input("Enter your age: "))

if age >= 18:
    print("You qualify for the credit card")
elif age == 0:
    print("You haven't been born yet!:")
elif age < 0:
    print("Please type your real age")
else:
    print("You must be 18+ to signup")