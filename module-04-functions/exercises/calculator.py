import math

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return 'Error: Division by zero'
    return a / b

def power(a, b):
    """Raise a to power of b"""
    return a ** b

def square_root(a):
    """Calculate square root"""
    if a < 0:
        return 'Error: Cannot take square root of negative number'
    return math.sqrt(a)

def show_menu():
    """Display calculator menu"""
    print('\n===== Calculator =====')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Power')
    print('6. Square Root')
    print('7. Exit')
    print('=' * 22)

# Main program
while True:
    show_menu()
    choice = input('Choose operation: ')
    
    if choice == '7':
        print('Goodbye!')
        break
    
    if choice == '6':
        num = float(input('Enter number: '))
        result = square_root(num)
    else:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = power(num1, num2)
        else:
            result = 'Invalid choice'
    
    print('Result:', result)
