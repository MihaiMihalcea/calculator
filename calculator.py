import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print("hi world")
clearConsole()

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return round((a / b), 2)

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculus(a, b):
    if operation == "+":
        return add(a, b)
    if operation == "-":
        return subtract(a, b)
    if operation == "*":
        return multiply(a, b)
    if operation == "/":
        return divide(a, b)

def calculator():
    a = int(input("What's your first number?: "))

    for keys in operations:
        print(keys)

    should_continue = True

    while should_continue:
        operation = input("Select your operation: ")
        b = int(input("What's your second number?: "))
        calculation_function = operations[operation]
        answer = calculation_function(a, b)
        print(f"{a} {operation} {b} = {answer}")
        if input(f"Type Y to continue calculating with {answer}, or N to start a new calculation: ") == "Y":
            a = answer
        else:
            should_continue = False
            clearConsole()
            calculator()

calculator()