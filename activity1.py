print("A CALCULATOR!")

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

print("Calculator functions")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
 
try:
        choice = input("Choose an operation (1-4 or q): ").strip().lower()

        if choice == "q":
            print("Goodbye!")
         

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
            if result == float("inf") or result == float("-inf"):
                print("(Product reached infinity!)")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or q.")

except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
except ZeroDivisionError:
        print("Error: Cannot divide by zero.")