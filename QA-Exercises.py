# Here is a complete log of all the challenge exercises for the topics we learn under Python at QA.
# These have been seperated by topics, and can be accessed through the terminal when run.
# Please note, these have not been black tested, and only white tested to check it works as intended.
# Please also note some functionality has been spread over multiple lines to make it easier to revise. 

# Introduction Exercise:
# Polite Program
# Create a python file that will input your first name, last name and outputs "Hello [firstname] [lastname]"

def introduction_exercise():
    fnvar = input("Please input your first name: ")
    lnvar = input("Please enter your last name: ")
    print(f"Hello {fnvar} {lnvar}.")

# Collections Exercise:

# In a new python file:
# Initialise a new 'books' dictionary, with author names as keys and lists of book titles as values.
# Write a program which asks the user for an author name and prints, as a string, the list of books by that author (hint: remember the join() method).
# Stretch goal: Display the list of books in alphabetical order

# import itertools                                                                                                                                                                  #used with bl list
def collections_exercise():
    books = {"Leo Tolstoy":["Anna Karenina", "Childhood", "Biography"], "Gustav Flaubert":["Madame Bovary"], "Vladimir Nabokov":["Lolita"],                                         #Here we have stored books in lists, under author keys; the list was needed in hindsight to allow multiple results, as each author must be unique to the book sets
             "Mark Twain":["The Adventures of Huckleberry Finn"]}
    
    print(f"Please see the following list of authors: {tuple(books.keys())}")                                                                                                       #outputting the authors into a tuple
    user_selection = input(f"please type an authors full name, to search what books they have produced: ")
    if user_selection in books.keys():                                                                                                                                              #This tests if True, you don't type "== True"
        print(f"{user_selection} has produced the following books: {books[user_selection]}")                                                                                        #searching for the author
    else:
        print("Unfortunately no books were found under that author")
    bl = list(books.values())
    # bl = list(itertools.chain.from_iterable(bl))                                                                                                                                  #This intertools.chain.from_iterable is used to unpack from [ , , ], [],[]... into 1 list, which  we can then sort  however the sum below does this better
    # print(bl)
    result = sum(bl, []) 
    print(f"Before sorting: {result}")                                                                                                                                              #This compiles [ , , , ],[ , , ],[] into 1 list, same as 34 but with less code called = more efficient
    print(f"After Sorting: {sorted(result)}")

#Conditionals Exercise:

# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"

def conditionals_exercise():
    user_input = int(input("Please enter the mark you have received: "))                                                                                                            
    if user_input >= 86:
        print("Distinction")
    elif user_input >= 65:                                                                                                                                                          #elif used instead of and statements for ease of writing
        print("Pass")
    elif user_input <= 64:
        print("Fail")


# Iteration Exercise:

# Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"


# I have done this in both while and range loops

def iteration_exercise_while():
    user_input = []
    counter = 0
    while counter != 5:
        user_input.append(input(f"Please enter name number {counter + 1}: "))
        counter = counter + 1
    counter = 0
    while counter != 5:
        print(f"{user_input[counter]} is awesome!")
        counter = counter + 1

def iteration_exercise_range():                                                                                                                                                     #This works the same as above, except the range() function is used to determine the loop iteration
    user_input = []
    for counter in range(5):
        user_input.append(input(f"Please enter name number {counter + 1}: "))
    for counter in range(5):
        print(f"{user_input[counter]} is awesome!")

# Work out what the following for loop does:
def iteration_challenge():
    for i in range(10, 21, 2):                                                                                                                                                      #counts from 10, to 21, in intervals of 2
        print(i)

# Functions Exercise:

# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.

# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.

# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def functions_exercise():
    b = "no"                                                                                                                                                                        #used to break loop.
    scores = {}                                                                                                                                                                     #empty dict.
    print("Once you have finished adding student scores, please type 'finished'")
    while b != "yes":                                                                                                                                                               #checking for break.
        sn = ""                                                                                                                                                                     #empty local variable for each loop iteration, used to store the different inputs.
        hs = ""
        ass = ""
        fes = ""
        
        sn = input("Please enter the students name: ")                                                                                                                              
        if sn != "finished":                                                                                                                                                        #checking if we need to exit the loop, done at each stage in case user needs to exit midway due to a mistake etc.
            hs = input("Please enter the students homework score: ")
        if sn != "finished" and hs != "finished":                                                                                                                                   #checking if we need to exit the loop, done at each stage in case user needs to exit midway due to a mistake etc.
            ass = input("Please enter the assessment score: ")
        if sn != "finished" and hs != "finished" and ass != "finished":                                                                                                             #checking if we need to exit the loop, done at each stage in case user needs to exit midway due to a mistake etc.
            fes = input("Please enter the final exam score: ")
        if sn == "finished" or hs == "finished" or ass == "finished" or fes == "finished":                                                                                          #check if we need to exit, 
            b = "yes"                                                                                                                                                               #if so, b variable set to "yes".
        if sn != "finished" and hs != "finished" and ass != "finished" and fes != "finished":                                                                                       #checking to make sure we need to append, if we are exiting the loop we don't want to append the current entries.
            scores[sn] = hs,ass,fes                                                                                                                                                 #appends local variables to dict record as {[sn]:[hs, ass, fes]}.
            print(f"Scores added for {sn}.")
    print("You have now finished entering scores")
    print(scores)

        

# CALLING FUNCTIONS-------------------------------------------------------------------------------------------------------------------------------------------------------------
# introduction_exercise ()
# collections_exercise()
# conditionals_exercise()
# iteration_exercise_while()
# iteration_exercise_range()
# iteration_challenge()
functions_exercise()
