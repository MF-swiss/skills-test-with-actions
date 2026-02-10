# System Modules
import math

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def get_nth_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
