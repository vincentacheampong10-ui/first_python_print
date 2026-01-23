# Python Calculator
import math

num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))

operator = input("Choose an operator(+ - * /): ")

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"The {operator} is not Valid")
