import math

def count_area(*args):
    num_args = len(args)
    
    if num_args == 2:  # Rectangle: requires 2 inputs (length, width)
        length, width = args
        return length * width
    
    elif num_args == 1:  # Circle: requires 1 input (radius)
        radius = args[0]
        return math.pi * radius ** 2
    
    elif num_args == 3:  # Triangle: requires 3 inputs (sides a, b, c)
        a, b, c = args
        s = (a + b + c) / 2  # Semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
        return area
    
    else:
        raise ValueError("Invalid number of arguments. Provide 1, 2, or 3 arguments.")

# მაგალითები:
print(count_area(5, 10))  # Rectangle: 50
print(count_area(7))      # Circle: 153.93804002589985
print(count_area(3, 4, 5))  # Triangle: 6.0
