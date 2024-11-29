"""
a slightly more complex algorithm
problem 3: finding the maximum of three numbers
"""
#write function -> find_max_of_three
#takes three integers as input and returns the largest of the three
#input num1, num2,num3
#output the largest of the three
#took me two minutes to write up the problem in my own words

def find_max_of_three(num1,num2,num3):
    """
    This function returns the largest of the three integers
    Parameters:
    num1,num2,num3 of type(int):The three integers to compare
    Returns:
    Int:the largest of the three integers
    """
    #a more efficitent method with a cleaner approach
    return max(num1,num2,num3)
