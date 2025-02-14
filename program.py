# Hunter Martin
# COSC 341 Winter 25'
# 2-13-25
# Simple python methods
import math
def compute_pi(n):
    result = 0
    for i in range(n):
        #alternates between adding and subtracting 1/ (2 * i + 1)
        if i % 2 == 0:
            result += (1 / (2 * i + 1))
        else: 
            result -= (1 / (2 * i + 1))

    #at the end take our result and multiply by 4
    result = result * 4
    return result

def compute_sqrt(x):
    last = 0.0 
    next = 1.0
    for i in range(10):
        last = next
        next = 0.5*(last + x / last)

    return next

def is_prime(n):
    maxNumberOfDivisors = 2
    divisors = 0
    #loop up to whatever n is 
    for i in range(1, n + 1, 1):
        if n % i == 0:
            divisors += 1
    
    #if we have more than 2 divisors then the number is NOT prime
    if(divisors > maxNumberOfDivisors):
        return False

    return True

def display_primes(n):
    #loop up to n and check every number and if its prime print the number
    for i in range(2, n + 1 , 1):
        if(is_prime(i)):
            print(str(i) + ',', end = '')

def process_scores():
    #I picked a large unrealistic number to represent the min score
    minScore = 999999
    maxScore = 0
    userWithMaxScore = ""
    userWithMinScore = ""
    count = 0 
    sumOfScores = 0
    while(True):
        user = input("Please enter your name and score (type q to quit): ")

        #split the name and score by a space
        user = user.split(" ")
        name = user[0]

        #if the user enter 'q' then we need to break out we are done
        if name == "q":
            break

        #need to cast into string since user[1] currently holds a string
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

def compute_tax(income, status, state):
        #change the status and state to all lowercase so we can ignore the case
        status_lowercase = status.lower()
        state_lowercase = state.lower()
        tax_rate = 0

        #lets deal with single first
        if status_lowercase == "single":
           if income < 30000: 
               tax_rate = .20
           elif income >= 30000:
               tax_rate = .25
        
        #married cases
        elif status_lowercase == "married":
            if income < 50000:
                tax_rate = .10
            elif income >= 50000:
                tax_rate = .15
        
        #if the user is out of state then minus 3% from the tax rate
        if(state_lowercase == 'o'):
            tax_rate -= .03

        return income * tax_rate

def solve_quadratic(a,b,c):
    #before anything we need to check if we have any solutions by doing b^2 - 4ac
    if math.pow(b,2) - (4 * a * c) >= 0:
        addition_solution = (-b + math.sqrt(math.pow(b,2) - (4 * a * c))) / 2 * a
        subtraction_solution = (-b - math.sqrt(math.pow(b,2) - (4 * a * c))) / 2 * a
    
    #we only have one solution the plus/minus is the same result
    elif math.pow(b,2) - (4 * a * c) == 0:
        addition_solution = (-b + math.sqrt(math.pow(b,2) - (4 * a * c))) / 2 * a
        subtraction_solution = addition_solution
    
    #if the I think the term is called determinant is < 0 then there are no solutions and the result is set to 0
    else:
        addition_solution = 0
        subtraction_solution = 0
    
    return addition_solution, subtraction_solution

def sort(list):
    #selection sort!!

    for i in range(0,len(list) - 1):
        mininum = i
        for j in range(i+1, len(list)):
            if list[j] < list[mininum]:
                mininum = j
        
        #simple swapping
        temp = list[i]
        list[i] = list[mininum]
        list[mininum] = temp

def id_password(first, last):
    #convert the first and last name to all uppercase because thats the requirement
    first_upper = first.upper()
    last_upper = last.upper()

    #we are going to concat to these strings
    id = ""
    password = ""

    #grab the first letter off first name and the rest of the last name
    id += first_upper[0]
    id += last_upper

    #grab the first letter of first name and the last letter of the last name
    password += first_upper[0]
    password += first_upper[len(first_upper) - 1]

    #grab the first 3 letters of the last name with a simple for loop
    first_three_letters_last = ""
    for i in range(3):
        first_three_letters_last += last_upper[i]

    password += first_three_letters_last
    password += str(len(first))
    password += str(len(last))
    print(id)
    print(password)

def file_sort(infile,outfile):
    #open the input and output file
    input_file = open(infile , 'r')
    output_file = open(outfile, 'w')

    #3 empty arrays/lists
    id = []
    name = []
    gpa = []

    #read the first line as an int, and that will represent how many students we are going to use
    line_number_of_students = input_file.readline()
    line_number_of_students= line_number_of_students.strip()
    number_of_students = int(line_number_of_students)

    for i in range(number_of_students):
        #read the line, then strip the \n character, then split (split on default, splits by spaces)
        line = input_file.readline()
        line = line.strip()
        line = line.split()

        #insert to the end of the list every time
        id.insert(len(id), int(line[0]))
        name.insert(len(name), str(line[1]))
        gpa.insert(len(gpa), float(line[2]))

    #selection sort again by id
    for i in range(0, len(id) - 1):
        mininum = i
        for j in range(i + 1, len(id)):
            if id[j] < id[mininum]:
                mininum = j

        temp = id[mininum]
        id[mininum] = id[i]
        id[i] = temp

        temp2 = name[mininum]
        name[mininum] = name[i]
        name[i] = temp2

        temp3 = gpa[mininum]
        gpa[mininum] = gpa[i]
        gpa[i] = temp3

    #prints the results to the output file
    output_file.write(str(number_of_students) + "\n")
    for i in range(number_of_students):
        output_file.write(str(id[i]) + " " + str(name[i]) + " " + str(gpa[i]) + "\n")
    
    input_file.close()
    output_file.close()

def display_menu():
    print("1. compute pi up to a certain number ")
    print("2. find the square root of a number ")
    print("3. display all the primes up to that number ")
    print("4. process scores ")
    print("5. compute tax ")
    print("6. solve quadratic solutions ")
    print("7. sort an array of numbers ")
    print("8. print an id and password ")
    print("9. sort a file of students by id ")
    print("10. quit")
    print("11. test the rectangle methods")
    
# Write a main program that allows a user to use the functions in questions 1-9. The
# program contains an interactive menu with 10 options. The user enters an option number
# to choose an option. Each option calls its function. If the function needs inputs then the
# menu program asks the user for inputs. If the function gives outputs then the menu
# program displays the outputs with appropriate messages. The menu program repeatedly
# displays the menu and asks for an option until the user decides to quit.
def main():
   keep_going = True
   while keep_going:
    display_menu()
    choice = int(input())
    if(choice == 1):
        n = int(input("Please enter a number to compute pi up to: "))
        print(compute_pi(n))
    elif(choice == 2):
        n = int(input("Please enter a number to find the sqrt of: "))
        print(compute_sqrt(n))
    elif(choice == 3):
        n = int(input("Please enter a number to display all the primes up to that number: "))
        display_primes(n)
        print()
    elif(choice == 4):
        process_scores()
    elif(choice == 5):
        income = int(input("Please enter your income "))
        status = str(input("Please enter your marital status (married or single) "))
        in_state = input("Please enter either 'o' for out of state or 'i' for in state ") 
        print("Your tax amount is $%.2f" % compute_tax(income, status, in_state))
    elif(choice == 6):
        a = int(input("Please enter a number representing 'a' "))
        b = int(input("Please enter a number representing 'b' "))
        c = int(input("Please enter a number representing 'c' "))
        addition_answer , subtract_answer = solve_quadratic(a,b,c)

        if(addition_answer == 0 and subtract_answer == 0):
            print("Sorry there were no solutions. ")
            
        #the plus/minus is the same answer 
        elif(addition_answer == subtract_answer):
            print(addition_answer)

        else:
            print(addition_answer)
            print(subtract_answer)
    elif(choice == 7):
        number_of_numbers_in_list = int(input("How many number are we sorting today"))
        nums = []
        for i in range(0, number_of_numbers_in_list):
            n = int(input("Please enter a number "))
            nums.insert(len(nums), n)

        sort(nums)
        for i in range(len(nums)):
            print(str(nums[i]) + ",", end= '')

        print()

    elif(choice == 8):
        first = str(input("What is your first name "))
        last = str(input("What is your last name: "))
        id_password(first, last)

    elif(choice == 9):
        input_file = str(input("What is the name of your input file (with .txt) "))
        output_file = str(input("What is the name of your output file (without .txt) "))
        file_sort(input_file,output_file)

    elif(choice == 10):
        print("Goodbye!")
        break

    elif(choice == 11):
        length = int(input("Please enter a length for your rectangle "))
        width = int(input("Please enter a width for your rectangle "))
        rectangle = Rectangle(length, width)
        print("The area for your rectangle is " + str(rectangle.area()))
        print(rectangle)

    else:
        print("Invalid input try again")


class Rectangle:
    def __init__(self,length, width ):
        self.length = length
        self.width = width

    #setters for length and width
    def setLength(self, length):
        self.length = length
    
    def setWidth(self, width):
        self.width = width

    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    def area(self):
        return self.length * self.width
    
    def __str__(self):
        return "Rectangle's length is " + str(self.length) + " and the width is " + str(self.width)
    


main()
