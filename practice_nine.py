"""
Problem 9(valid anagram)

write a function -> is_anagram

takes two strings as inputs and determines if they are anagrams
Two strings are considered anagrams if they contain the same characters in 
the same frequency but in any order.
"""
#input two strings, s and t
#output a boolean
#True if the strings are anagrams
#False otherwise
# def is_anagram(s,t):
#     string_s = []
#     for char in s:
#         string_s += char
#     string_t = []
#     for char in t:
#         string_t += char
#     for anagram_possible in string_s:
#         if anagram_possible in string_t:
#             return True
    # return False #I know this is the most ridiculous code 
#I have ever written and should never work in whatever universe,
#  this is beyond half baked,
#  this completely charred and burned beyond comprehension and
    #should not ever be used in a public data base

#Key characteristic of an Anagram
"""
They must have the same length.
Each character in one string must appear in other string the same number of times

"""

"""
A much better structured way
1.Check lenghts 
-if the lengths of s and t are different, they can't be anagrams
2.Count character Frequencies
-use a fequency counter (like a dict or collections.Counter) to count the number 
of times each character appears in both strings.
3.Compare Frequenceis 
-if the frequency distribution of the two strings are identical, they are anagrams
we will implement two solutions for this kind of problem

"""
from collections import Counter
def is_anagram(s,t):
    """
    Determines if two strings are anagrams.

    Parameters:
    s (str): The first string.
    t (str): The second string.

    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
#Alternative solution without collections.Counter
def is_anagram_alternative_solution(s,t):
    if len(s) != len(t):
        return False
    
    #create a frequency dictionaries for both strings 
    char_count_t ={}
    char_count_s ={}
    for char in  s:
        char_count_s[char] = char_count_s.get(char,0) + 1
    for char in t:
        char_count_t[char] = char_count_t.get(char,0) + 1
    
    #compare the two dictionaries
    return char_count_s == char_count_t
