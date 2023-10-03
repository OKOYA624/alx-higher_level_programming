#!/usr/bin/python3
import random
import random

# Generate a random signed number
number = random.randint(-10, 10)

# Check if the number is positive, zero, or negative
if number > 0:
    result = "is positive"
elif number == 0:
    result = "is zero"
else:
    result = "is negative"

# Print the number and its classification
print(f"{number} {result}")

