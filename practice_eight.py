"""
Problem 8: a function called move_zeroes
function -> takes a list of integers and moves all the zeroes to the end
of the list while maintaining the relative order of the non zero elements 
"""
#input A list of integers num
#The same list with all zeroes moved to the end
#took me 20 minutes to come up with this half baked solution, don't even know where to start lmaoo😂
"""
first -> identify non zero elements 
iterate through the list and find all  the non zero elements. These elements 
should stay in their relative order

2.Move non-zero elements to the front
use a pointer (write index ) to keep track of where to write the next non-zero 
element as you iterate through the list

3.Fill the remaining Positions with Zeroes
once all non-zero elements are writen to the front of the list, fill the rest with zeroes
"""
def move_zeroes(nums):
    """
    Moves all zeroes in the list to the end while maintaining the relative
    order of non-zero elements.

    Parameters:
    nums (list): List of integers to rearrange.

    Returns:
    None: The function modifies the list in-place.
    """
    write_index = 0 #pointer to track where to write the next non-zero number
    for num in nums:
        if num != 0:
            nums[write_index] = num # we go to the first index and overwrite any value in there with num
            write_index += 1
    for i in range(write_index,len(nums)): #range will exclude the final index
        nums[i] = 0