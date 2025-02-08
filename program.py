import math
# # Write a function that computes the value of mathematical constant π. The value of π
# can be computed using the infinite series p = 4(1 – 1/3 + 1/5 – 1/7 + 1/9
# – 1/11 + . . .). The function compute_pi(n) computes the value of π using
# the first n terms of the infinite series and returns the value
def compute_pi(n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result += (1 / (2 * i + 1))
        else: 
            result -= (1 / (2 * i + 1))

    result = result * 4
    return result

#  Write a function that computes the square root of a given number. The square root of a
# number x can be computed as follows. First guess that the square root of x is 1. Then
# repeatedly get the next guess from the last guess using the relation next = 0.5(last + x
# / last) where last is the last guess and next is the next guess. Repeat ten times using
# a loop and the tenth guess will be the square root. The function compute_sqrt(x)
# computes the square root of x and returns the square root
def compute_sqrt(x):
    last = 0.0 
    next = 1.0
    for i in range(10):
        last = next
        next = 0.5*(last + x / last)

    return next

# . Write a function that decides whether a given number is a prime or not. A prime
# number is a number that is divisible only by 1 and itself. The function is_prime(n)
# decides whether n is prime or not and returns true if n is prime and returns false
# otherwise. Write another function display_primes(n)that displays all prime
# numbers less than or equal to n
def is_prime(n):
    maxNumberOfDivisors = 2
    divisors = 0
    for i in range(1, n + 1, 1):
        if n % i == 0:
            divisors += 1
    
    if(divisors > maxNumberOfDivisors):
        return False

    return True

def display_primes(n):
    for i in range(1, n + 1 , 1):
        if(is_prime(i)):
            print(str(i) + ',', end = '')

# Write a function process_scores( )that reads student names and their scores
# from a user and displays the following: the average score, the minimum score, the
# maximum score, and the students who received the minimum and maximum scores. The
# function repeatedly prompts the user to enter the name and the score of a student. The
# user enters the name and the score separated by blank in one line. The name is a single
# word and the score is an integer. The user enters q in lower or upper case to quit. The
# user does not enter score after q. The outputs are displayed with appropriate messages.
def process_scores():
    minScore = 999999
    maxScore = 0
    userWithMaxScore = ""
    userWithMinScore = ""
    count = 0 
    sumOfScores = 0
    while(True):
        user = input("Please enter your name and score (type q to quit): ")
        user = user.split(" ")
        name = user[0]
        if name == "q":
            break
        score = int(user[1])
        count += 1
        sumOfScores += score
        if maxScore <= score:
            maxScore = score 
            userWithMaxScore = name
        if minScore >= score:
            minScore = score 
            userWithMinScore = name

    print("The user with the lowest score of " + str(minScore) + " is " + userWithMinScore)
    print("The user with the highest score of " + str(maxScore) + " is " + userWithMaxScore)
    print("The average score of all the users is " + str(sumOfScores/count))




def main():
   # n = int(input("Please enter a number to find primes upto "))
    #display_primes(n)
    process_scores()


main()
