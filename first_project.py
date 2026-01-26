# While loops

name = input("What is your name: ")

while name == "":
    print("You did not enter your name")
    name = input("What is your name: ")

    print(F"Hello {name}")
