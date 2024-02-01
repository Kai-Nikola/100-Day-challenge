# Exercise 1
print("Hello World")

# Exercise 2
my_string = "Hello"
print(len(my_string))

# Exercise 3.1
user_input = int(input("Number: "))
if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 3.2
for square in range(1, 6):
    square *= square
    print(square)


# Exercise 4.1
def calculate_area(radius):
    return 3.14 * radius * radius


print(calculate_area(10))

# Exercise 4.2
def multiply_numbers(number1, number2, number3):
    return number1 * number2 * number3

print(multiply_numbers(4, 5, 6))

# Exercise 5.1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for fruit in fruits:
    print(fruit)

# Exercise 5.2
def find_max():
    numbers = [1, 2, 3, 4, 5]
    largest = []
    for number in numbers:
        largest = largest.append(number)
    return max(largest)

print(find_max())

# Exercise 5.3
person = {
    "name" = "Josh",
    "age": 15,
    "city" = "LA"
}

for values in person:
    print(values, person[values])

# Excersie 6
try:
    num1 = int(input("Num1: "))
    num2 = int(input("Num2: "))
    result = num1/num2
except (ZeroDivisionError, ValueError):
    print("Errors thrown")

