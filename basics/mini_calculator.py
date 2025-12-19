# basics/mini_calculator.py

a = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "Error: division by zero"
    else:
        result = a / b
else:
    result = "Error: unknown operation"

print("Result:", result)
