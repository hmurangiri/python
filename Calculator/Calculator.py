import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero"

def power(num1, num2):
    return num1 ** num2

def square_root(num):
    return math.sqrt(num)

def logarithm(num):
    return math.log10(num)

def calculate_percentage(num, percentage):
    return (num * percentage) / 100

def calculate_average(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return "Error: No numbers provided"

def calculator():
    print("Welcome to the Calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Percentage")
    print("9. Average")
    print("10. Exit")
    
    while True:
        operation = input("Enter the operation number (1-10): ")

        if operation == "10":
            print("Exiting the calculator...")
            break

        if operation not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid operation. Please try again.")
            continue

        if operation == "6":
            num = float(input("Enter a number: "))
            result = square_root(num)
            print(f"Square root of {num} = {result}")
        elif operation == "7":
            num = float(input("Enter a number: "))
            result = logarithm(num)
            print(f"Logarithm of {num} = {result}")
        elif operation == "8":
            num = float(input("Enter the number: "))
            percentage = float(input("Enter the percentage: "))
            result = calculate_percentage(num, percentage)
            print(f"{percentage}% of {num} = {result}")
        elif operation == "9":
            numbers = []
            while True:
                num = float(input("Enter a number (or 0 to calculate average): "))
                if num == 0:
                    break
                numbers.append(num)
            result = calculate_average(numbers)
            print("Average:", result)
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            result = 0

            if operation == "1":
                result = add(num1, num2)
            elif operation == "2":
                result = subtract(num1, num2)
            elif operation == "3":
                result = multiply(num1, num2)
            elif operation == "4":
                result = divide(num1, num2)
            elif operation == "5":
                result = power(num1, num2)

            print("Result:", result)

        save_result = input("Do you want to save the result? (yes/no): ")

        if save_result.lower() == "yes":
            with open("calculator_results.txt", "a") as file:
                file.write(f"{num1} {operation} {num2} = {result}\n")
