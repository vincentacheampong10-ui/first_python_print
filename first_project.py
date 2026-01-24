# Logical operators = OR, AND, NOT

temp = 25
is_raining = False


# OR
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event has been cancelled")
# else:
#     print("The outdoor event is still scheduled")


# AND
# if temp < 35 and is_raining:
#     print("The outdoor event has been cancelled")
# else:
#     print("The outdoor event is still scheduled")

# Not
if temp < 35 and not is_raining:
    print("It's cold outside today ")
elif 65 < temp < 75:
    print("Tt is warm outside")
elif 75 > temp <95:
    print("It is very hot outside")
