# varNum = 1500

# # while varNum < 2600:                                                                                                                        #loop

# #     varNum += 1                                                                                                                             #count

# # the better way to loop for ranges:

# https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

#1: Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# Num_Store = []                                                                                                                                #This variable is a list []

# for x in range (1500,2701):                                                                                                                   #A for loop using this range function, which loops till 2700, 2701 isn't accepted into loop
#     if (x%7==0) and (x%5==0):                                                                                                                 #Modulo, dividing outputs the remainder, if 0 then we know its a whole number and the number is indeed divisible
#         Num_Store.append(str(x))                                                                                                              #Apends number to the list

# print(' '.join(Num_Store))  

#                                                                                                                                               #Outputs the result with a ' ' in between items

#2: Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

# def temp_convert (input_temp, input_type):
#     if input_type == 'C':
#         new_temp = (input_temp / 9)*9
#         return new_temp
        
#     elif input_type == 'F':
#         return("inputted is F")


# temp_in_temp = int(input("Please input the temperature: "))
# temp_in_type = str(input("Please input temp type - C or F? "))
# temp_result = temp_convert(temp_in_temp, temp_in_type)
# print (temp_result)


#4: Write a Python program to guess a number between 1 to 9. 
# from random import randint
# comp_num = randint(1,9)
# player_guess = input("Please choose a guess a number between 1 and 9")
# if player_guess != comp_num:
#     if playerguess > comp_num:
#         print("Try a little lower")
#     elif playerguess < comp_num:
#         print ("Unlucky, try a bit higher")
# elif player_guess == comp_num
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exercises
# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.

# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.

# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

# def student_grade(student_name, homework_score, assessment_score, exam_score):                                                                   #Function with varables
#     total_score = homework_score + assessment_score + exam_score                                                                                 #Total score
#     percentage_score = (total_score / 175) * 100                                                                                                 #Total percentage
#     return percentage_score                                                                                                                      #Return Value
   

# in_student_name = str(input("What is your name? "))                                                                                              #input saved as var
# in_homework_score = int(input("What is your homework score out of 25? "))                                                                        #input saved as var
# in_assessment_score = int(input("What is your assessment score out of 50? "))                                                                    #input saved as var
# in_exam_score = int(input("What is your exam score out of 100? "))                                                                               #input saved as var

# flo_percentage_grade = student_grade(in_student_name, in_homework_score, in_assessment_score, in_exam_score)                                     #Takes percentage_score returned from student_grade and saves it to a global var we can use                               
# print(flo_percentage_grade)                                                                                                                      #prints out new global variable we've made in line above

# Write a Python function to find the Max of three numbers
# Write a function
# Three numbers
# function needs to take three numbers
# Find the maximum


# def Maximum(num1, num2, num3):
#     if num1 > num2:
#         if num1 > num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2 > num3:
#             return num2
#         else:
#             return num3

# in_num1 = int(input("Please input the first number you would like to compare: "))
# # in_num2 = int(input("Please input the second number you would like to compare: "))
# # in_num3 = int(input("Please input the third number you would like to compare: "))
# # pri_max = Maximum(in_num1, in_num2, in_num3)
# # print(pri_max)

from random import randint