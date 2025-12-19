# basics/input_output.py

name = input("Enter your name: ")
age_str = input("Enter your age: ")

# input() returns string, so convert to int
age = int(age_str)

print("\n--- Summary ---")
print("Hello,", name)
print("Next year you will be", age + 1)
