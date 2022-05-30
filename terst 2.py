# print("hello friend")
# name = "LLAMA"
# print("my name is " + name)
# print("my name is {}".format(name))
# print(f"my name is {name}")
# ctrl / will comment all lines selected



#Global Variables:
user_selection = int(0)




#Main menu
print ("=========================================================================================================================================================================")
print ("Hello! And welcome, to the introductory project showcase, hosted by LLAMA")
print ("Below you will see a list of beginner projects created for your enjoyment. Please select one of the following projects by entering the number listed for that project.")
print ("For example if you want to open the first project listed, simply type '1'")
print ("1 - Madlibs game")
while user_selection == 0:

    user_selection = input ("Please enter your selection ")

    user_selection = int (user_selection)

    print (user_selection)
    if user_selection == 1:
        # This is a basic Madlib project
        adj = input("Adjective ")
        verb = input("Verb ")
        advised_projects = input("Advised projects for improvement ")

        madlib = f"Computer programming is {adj}! Often I find reading beginner projects makes me want to {verb}. Personally I would recommend completing projects which focus on {advised_projects}."

        print (madlib)

    #Random Number Game

    if user_selection == 2:
        


    if user_selection != 1 or 2:
        user_selection = 0
        print ("I am sorry, the value you have entered is incorrect - please type the number of the game you wish to play.")
        print ("1 - Madlibs game")
        user_selection = input ("Please enter your selection ")