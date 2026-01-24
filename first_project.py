# Conditional Expression

num = 5
a = 55
b = 7
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
max_num = a if a > b else b
print(max_num)

print("Access allowed" if user_role == "admin" else "Access denied")