"""
Problem 4:Leap Year Checker
function -> is_leap_year
-it is divisible by 4 
-but not divisible by 100 unless it is also divisible by 400
"""
#function takes num of type(int)
#outputs True if the year is a leap year 
#outputs False otherwise

def is_leap_year(num):

    # if num % 4 ==0 and num > 0:
    #   if num % 400 ==0:
    #         return True
    #   elif num % 100 == 0:
    #         return False
     
    # else:
    #     return False
    #this has taken me 7 minutes and 44 seconds to complete

    # more streamlined version would be 
    # return num > 0 and (num % 4 == 0 and (num % 100 != 0 or num % 400  == 0)) #real triky
    #another solution would be:
    if num % 4 == 0:
        if num % 100 == 0:
            return num % 400 == 0#this can evaluate and return either True or False
        return True
    return False