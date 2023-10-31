import math
import requests
import os


def calculate_factorial(num):
    return math.factorial(num)


number = 5
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")

r = requests.get("http://stephaniehicks.com")
print(r.status_code)

name = input("name? ")
print("Hello, ", name) 