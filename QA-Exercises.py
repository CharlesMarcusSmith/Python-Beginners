# Here is a complete log of all the challenge exercises for the topics we learn under Python at QA.
# These have been seperated by topics, and can be accessed through the terminal when run.
# Please note, these have not been black tested, and only white tested to check it works as intended.

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

def collections_exercise():
    books = {"Leo Tolstoy":["Anna Karenina", "Childhood", "Biography"], "Gustav Flaubert":["Madame Bovary"], "Vladimir Nabokov":["Lolita"],                                     #Here we have stored books in lists, under author keys; the list was needed in hindsight to allow multiple results, as each author must be unique to the book sets
             "Mark Twain":["The Adventures of Huckleberry Finn"]}
    
    print(f"Please see the following list of authors: {tuple(books.keys())}")                                                                                                   #outputting the authors into a tuple
    user_selection = input(f"please type an authors full name, to search what books they have produced: ")
    if user_selection in books.keys():                                                                                                                                              #This tests if True, you don't type "== True"
        print(f"{user_selection} has produced the following books: {books[user_selection]}")                                                                                        #searching for the author
    else:
        print("Unfortunately no books were found under that author")
        collections_exercise()





# Calling functions
# introduction_exercise ()
collections_exercise()