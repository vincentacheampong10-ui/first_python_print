# While loops

# age = int(input("How old are you: "))
#
# while age < 0:
#     print("Age cannot be negative ")
#     age = int(input("How old are you: "))
#
#     print(F"You are {age} years old")

food = input("Enter your favourite food(q to quit): ")

while not food == "q":
    print(f"Your favourite food is {food.capitalize()}.")
    food = input("Enter your favourite food(q to quit): ")

print("Bye, have a good day.")


