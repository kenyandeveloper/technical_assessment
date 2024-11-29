"""
problem 2 check even or odd

write a function 
called check_even_or_odd

takes a single integer as an input and returns 
"Even" if the number is even
"ODd" if the number is odd
"""

def check_even_or_odd(num):
    """
    this function checks wether a given integer is even or odd

    parameters:
    num of type(int): is the integer to check

    returns:
    a string "Even" if the number is even, "Odd" if the number is odd
    """
    return "Even" if num % 2 == 0 else "Odd"