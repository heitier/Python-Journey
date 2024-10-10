# Python Calculator Program

---

This is a simple Python-based calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division) between two numbers. The program allows users to continuously calculate using previous results or start new calculations.

## Features

- Supports four basic operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Prevents division by zero and returns an error message in such cases.
- Allows users to continue calculating with the result of the previous operation.
- Provides an option to start a new calculation or quit the program.
- Validates numeric input, ensuring that users enter valid numbers for the calculations.
- Includes a function to simulate clearing the console after each step for a better user experience in terminal environments.

## How It Works

1. The program asks the user for a number, an arithmetic operation, and another number.
2. It performs the selected operation and displays the result.
3. The user can:
   - Continue calculating with the previous result.
   - Start a new calculation.
   - Quit the program.
4. If an invalid input or operator is given, the program will notify the user.

## Example Usage

```bash
Enter first number: 10
Choose an operation: +, -, /, *: +
What's the next number: 5
15.0

Type 'y' to continue calculating with 15.0, 'n' to start a new calculation, or 'q' to quit: y
Choose an operation: * 
What's the next number: 3
45.0

Type 'y' to continue calculating with 45.0, 'n' to start a new calculation, or 'q' to quit: q
Goodbye!
```
## Code Structure

- **`add()`**, **`subtract()`**, **`multiply()`**, **`divide()`**: Functions that perform arithmetic operations.
- **`is_numeric()`**: Checks whether user inputs are valid numbers.
- **`control_calc()`**: Handles the logic for performing the appropriate calculation based on the chosen operation.
- **`first_prompt()`**: Prompts the user for inputs, including numbers and the chosen arithmetic operation.
- **`main()`**: The main loop of the program, allowing users to continue calculations, start fresh, or exit the program.

## Handling Edge Cases

- The program handles division by zero and returns an appropriate error message.
- If non-numeric input is provided, the program will prompt the user to enter a valid numeric value.
- Invalid operators result in an error message and prompt the user to enter a valid operation.

## Contributions

Feel free to fork the repository and submit pull requests if you would like to contribute to the project. All contributions are welcome!

---