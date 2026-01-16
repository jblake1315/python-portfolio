def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# Main program
print('Temperature Converter')
print('1. C to F')
print('2. F to C')

choice = input('Choose (1 or 2): ')

if choice == '1':
    c = float(input('Enter Celsius: '))
    f = celsius_to_fahrenheit(c)
    print(f'{c}C = {f}F')
else:
    f = float(input('Enter Fahrenheit: '))
    c = fahrenheit_to_celsius(f)
    print(f'{f}F = {c}C')