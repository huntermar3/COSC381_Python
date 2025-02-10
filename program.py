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
    for i in range(1, n + 1 , 1):
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


def main():
   # n = int(input("Please enter a number to find primes upto "))
    #display_primes(n)
   # process_scores()
   id_password("christian", "martin")
   file_sort("test.txt", "output.txt")


main()
