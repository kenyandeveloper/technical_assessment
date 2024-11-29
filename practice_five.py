"""
Problem 5 FizzBuzz.
"""
#write a function callad fizz_buzz
#function takes integer n as input and prints the numbers from 1 to n
#with the following values
#for a multiples of 3, print "fizz" instead of the number
#for multiples of 5  print "buzz" instead of the number
#for multiples of both 3 and 5, print "FizzBuzz"
#for all other numbers, print the number itself

def fizz_buzz(n):
    if n > 0: #handling edge case where n is 0

        for i in range(1,n+1): #be careful with using range
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
#took me seven minutes to write this up