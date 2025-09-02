import numpy as np
from datetime import date
import math 

#Example function using numpy
"""Calculates the area of a circle given its radius."""
def calculate_circle_area(radius):
    return np.pi * np.power(radius, 2)
print(calculate_circle_area(5))

#Example function using datetime
def days_until_new_year():
    """Calculates the number of days until the next New Year."""
    today = date.today()
    new_year = date(today.year + 1, 1, 1)
    return (new_year - today).days
print(days_until_new_year())

#Example function using arrays
def calculate_mean(numbers):
    """Calculates the mean of a list of numbers."""
    arr = np.array(numbers)
    return np.mean(arr)
print(calculate_mean([1, 2, 3, 4, 5]))

#Exapmle function manipulating arrays
def normalize_array(arr):
    """Normalizes a numpy array to have values between 0 and 1."""
    arr = np.array(arr)
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print(normalize_array([10, 20, 30, 40, 50]))

#Example function using math
def calculate_hypotenuse(a, b):
    """Calculates the hypotenuse of a right triangle given the lengths of the other two sides."""
    return math.hypot(a, b)
print(calculate_hypotenuse(3, 4))


