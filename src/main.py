# This program performs addition or subtraction of two numbers entered by the user

def get_number(prompt):
    """Prompt the user to enter a number and return it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    """Prompt the user to choose an operation and return it."""
    while True:
        operation = input("Enter '+' to add or '-' to subtract or '*'to multiply or '/' to divide: ").strip() # Trim spaces
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Invalid operation. Please enter '+' or '-' or '*' or '/'.")

def calculate(num1, num2, operation):
    """Perform the chosen operation and return the result."""
    print(f"Performing {operation} on {num1} and {num2}")
    if operation == '/':
        if num2 == float(0):
            return "Error: Division by zero is not allowed."
        return num1 / num2
    elif operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2      
    elif operation == '*':
        return num1 * num2
    
    
def main():
    """Main function to run the calculator program."""
    print("Welcome to the Simple Calculator!")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()
    print(f"You chose to {operation} the numbers {num1} and {num2}.")  
    # Perform the calculation
    result = calculate(num1, num2, operation)
    
    if operation == '+':
        print(f"The sum of {num1} and {num2} is: {result}")
    elif operation == '-':
        print(f"The difference between {num1} and {num2} is: {result}")
    elif operation == '*':
        print(f"The product of {num1} and {num2} is: {result}")
    elif operation == '/':
        print(f"The division of {num1} and {num2} is: {result}")

# Run the program
if __name__ == "__main__":
    main()