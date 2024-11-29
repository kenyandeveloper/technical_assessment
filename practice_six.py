"""
Reverse a string
"""
#function called -> reverse_string
#function takes a string as an input
#function returns the string 
# a better implementation would be:
def reverse_string(any_string):
    return any_string[::-1]
"""
start: Starting index (default is the beginning of the string).
stop: Ending index (default is the end of the string).
step: How much to increment (or decrement) the index.


By specifying [::-1]:

Start from the end (-1 as the step value means "go backward").
No start or stop is specified, so it goes from the end to the beginning of the string.
"""

# def reverse_string(any_string):
#     return "".join(reversed(any_string)) # i have understood why we need to do this



# #this solution adds unnecesary complexity
# def reverse_string(any_string):
#     store_word = []
#     for character_letter in any_string:
#         store_word.append(character_letter)
#     reversed_array = reversed(store_word)
#     return "".join(reversed_array)

#this has taken me seven minutes to come up with the solution