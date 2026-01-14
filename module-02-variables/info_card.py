# Portfolio Project 1: Personal Information Card
# Module 2: Variables and Data Types

print("===== Personal Information Card =====")
print()

# Get user information
name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("What city do you live in? ")
hobby = input("What is your favorite hobby? ")

# Display the card
print()
print("===== YOUR INFORMATION CARD =====")
print("Name:", name)
print("Age:", age, "years old")
print("City:", city)
print("Favorite Hobby:", hobby)
print()
print("Fun Fact: In 10 years, you will be", age + 10, "years old!")
print("================================")