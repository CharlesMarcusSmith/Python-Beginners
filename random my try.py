import random

def player_guess (x):
    random_number = random.randint (1,x)
    player_guess = 0
    
    while player_guess != random_number :
        player_guess = int ( input (f"Please guess a number between 1 and {x}: "))
        if player_guess < random_number :
            print ("Unlucky! That is not correct I'm afraid, please try again. Maybe try a little higher")
        elif player_guess > random_number :
            print ("Oh no! I'm afraid that is not correct, please try again. Maybe try a little lower")
    print ("Congratulations! Huray, you have guess the number correctly, well done.")

def machine_number (x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" :
        if low != high : #rand int will throw a error if the low and high are the same, which is why != is used to exit loop if so
            guess = random.randint(low, high) 
        else: 
            guess = low
        feedback = input(f"Is {guess} too high? (H), too low (L), or correct? (C)"). lower() # will lower case the string, comparison is case sensitive
        if feedback == 'h' : #lower case as it is lowered at the end of line above
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1
    print (f"Yay! The computer guessed your number, {guess}, correctly!")






player_guess (10)
machine_number (10)