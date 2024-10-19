import data_types
import datadog #install missing libraries with pip
import os

#randomnesss with random
import random

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Shuffle a list randomly
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")


# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# List files and directories in the current working directory
files = os.listdir(cwd)
print(f"Files in '{cwd}': {files}")


#file searching with glob
import glob

# Find all Python files in the current directory
python_files = glob.glob("*.py")
print(f"Python files in directory: {python_files}")

#math operations with math
import math

# Calculate the square root of a number
num = 16
sqrt_num = math.sqrt(num)
print(f"Square root of {num} is {sqrt_num}")

# Calculate sine of 90 degrees (converted to radians)
angle = 90
sine_value = math.sin(math.radians(angle))
print(f"Sine of {angle} degrees is {sine_value}")

#date and time handling with datetime
import datetime

# Get the current date and time
now = datetime.datetime.now()
print(f"Current Date and Time: {now}")

# Calculate a date 10 days from now
future_date = now + datetime.timedelta(days=10)
print(f"Date 10 days from now: {future_date}")
