# 1:
# # books = {"Darren Simpson":"Scavengers", "Jenny McCartney":"The Ghost Academy", "Anu Partanen":"The Nordic Theory Of Everything"}
# # var1 = input("Please state the author you wish to search: ")
# # print (books.var1)




# # Set up some vars
# devs_money = 100
# dev_can_play_smash = False

# # Conditional Statement to test vars

# #     number test            bool test
# #        True                   False       = False
# if devs_money > 10 and dev_can_play_smash:
#     print("Dev enters a smash tournament!")

# # Second Test
# #       False                   False       = False
# elif devs_money < 10 and dev_can_play_smash:
#     print("Dev is too poor to enter")

# # else Statement
# # True

# else:
#     print("Dev just can't play smash")

# print("Done")

# 2:
# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"

var1 = int(input("Please enter your mark: "))
if var1 >= 85:
    print("distinction")
elif var1 >= 65:
    print("pass")
else:
    print("fail")

