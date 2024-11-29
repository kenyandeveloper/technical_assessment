"""Problem 7:Palindrome Number.
function -> is_palindrome_number 
checks wether a given integer is a palindrome
A number is considered a palindrome if it reads the same forward and backward.
# """
# def is_palindrome_number(n):
#     if n >= 0:
#         new_list = [n]
#         reversed_list = reversed(new_list)
#         if reversed_list == new_list:
#             return True
#         return False # THIS IS ALL WRONG. IMPOSSIBLE!!
    
#wrote this solution in 8 minutes
"""
this solution has a problem
reversing an integer 
the reversed() function -> only works on iterables
iterables like strings or lists, not directly on integers
since the problem constraints prohibits converting the integer to a string,
we need a mathermatical approach to reverse the number
"""
# def is_palindrome_number(n):
#     if n < 0:
#         return False
#     #reverse the number mathematically 
#     original = n
#     reversed_num = 0
#     while n > 0:
#         last_digit = n % 10
#         reversed_num = reversed_num * 10 + last_digit # Build the reversed number
#         n //= 10  # Remove the last digit from the original number
#     return reversed_num == original

"""
so in this code above we have managed to reverse the integer using mathematical operations
we used 
-last_digit
-revered_num #buid the reversed num
-remove the last digit from the original number
"""
def is_palindrome_number(n):
    if n < 0:
        return False
    original_number = n
    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10
    return reversed_num == original_number