# Simple Calculator with Safety Check
print('===== Simple Calculator =====')
print()

# Get two numbers from user
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# Perform basic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Check if power operation is safe
if num2 <= 100:  # Only calculate power if exponent is reasonable
    power = num1 ** num2
else:
    power = "Too large to calculate!"

# Display results
print()
print('===== Results =====')
print('Addition:', num1, '+', num2, '=', addition)
print('Subtraction:', num1, '-', num2, '=', subtraction)
print('Multiplication:', num1, '*', num2, '=', multiplication)
print('Division:', num1, '/', num2, '=', division)
print('Power:', num1, '**', num2, '=', power)
