import random

def guess (x):      # defining the function 
    random_number = random.randint(1, x) # x here will be printed later
    guess = 0
    while guess != random_number:      # while loop
        guess = int (input(f'Guess a number between 1 and {x}: ')) # FIXME int () ensures input () is changed to an integer if possible - black test shows that inputting text instead of numbers caused errors when trying to ocnvert to in FIXME

        print (guess)
        if guess < random_number :
            print ("Incorrect, try a little higher.")
        # elif = else if
        elif guess > random_number :
            print ("Incorrect, try a little lower.")
    print (f"Congratulations! You have correctly guessed the random number {random_number}.")

