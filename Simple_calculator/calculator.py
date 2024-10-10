from art import logo  # Importing a logo (assumed to be ASCII art) from an external file or library.

# Define a function to add two numbers.
def add(n1, n2):
    return n1 + n2

# Define a function to subtract the second number from the first.
def subtract(n1, n2):
    return n1 - n2

# Define a function to multiply two numbers.
def multiply(n1, n2):
    return n1 * n2

# Define a function to divide the first number by the second.
# It checks if the divisor (n2) is 0 to avoid division by zero errors.
def divide(n1, n2):
    if n2 == 0:
        return "Error - Division by 0"
    return n1 / n2

# Define a function to check if the input is a numeric value.
# Returns True if it can be converted to a float, otherwise prints an error and returns False.
def is_numeric(value):
    """Checks if a value is numeric"""
    try:
        float(value)
        return True
    except ValueError:
        print("Please enter a numeric value")
        return False

# This function controls the calculation.
# It first checks if both numbers are valid numeric values.
# If they are, it looks for the operator in the dictionary and performs the appropriate operation.
def control_calc(num1, num2, ch_op):
    """Controls whether the operation is valid, and it's a numeric value and does the calculation"""
    if not is_numeric(num1) or not is_numeric(num2):
        return "Not a number"
    # Dictionary mapping operators to their corresponding functions.
    operation = {"+": add,
                 "-": subtract,
                 "/": divide,
                 "*": multiply
                 }
    # If the operator is valid, perform the operation, otherwise return an error message.
    if ch_op in operation:
        return operation[ch_op](num1, num2)
    else:
        return "Invalid operator. Please choose: +, -, /, *"

# Function to prompt the user for inputs (first number, operator, and second number).
# If no first number is provided, it will ask for one. Otherwise, it uses the result of a previous calculation.
def first_prompt(num1=None):
    if num1 is None:
        num1 = float(input("Enter first number: "))
    choose_op = input("Choose an operation: +, -, /, *: ")
    num2 = float(input("What's the next number: "))
    return num1, choose_op, num2

# Constant prompt message for asking whether to continue with the current calculation, start a new one, or quit.
CONTINUE_PROMPT = "Type 'y' to continue calculating with {}, 'n' to start a new calculation, or 'q' to quit: "

# Main function that runs the calculator.
def main():
    working = True  # Flag to keep the program running.
    while working is True:
        print(logo)  # Print the ASCII art logo at the start of each calculation session.

        # First prompt to get the initial number, operator, and second number.
        num1, choose_op, num2 = first_prompt()

        # Calculate the result using the provided inputs.
        answer = control_calc(num1, num2, choose_op)
        print(answer)  # Print the result of the calculation.

        # Ask if the user wants to continue with the current result, start a new calculation, or quit.
        redo = input(CONTINUE_PROMPT.format(answer)).lower()

        # If the user wants to continue with the current result, repeat the calculation.
        while redo == "y":
            num1, choose_op, num2 = first_prompt(num1=answer)  # Use the previous result as the first number.
            answer = control_calc(num1, num2, choose_op)  # Perform the calculation.
            print(answer)  # Print the updated result.
            redo = input(CONTINUE_PROMPT.format(answer)).lower()  # Ask again if they want to continue.

        # If the user chooses to quit, set the flag to False to exit the loop.
        if redo == "q":
            working = False
            print("Goodbye!")  # Print goodbye message when exiting.

        # If the user wants to start a new calculation, the screen is cleared and the loop restarts.
        elif redo == "n":
            print("\n" * 100)  # Simulate clearing the console (in terminal environments).

        # If the input is not recognized, prompt the user with an error.
        else:
            print("Invalid input. Please type 'y', 'n', or 'q'.")


# Run the main function if the script is executed (and not imported as a module).
if __name__ == "__main__":
    main()