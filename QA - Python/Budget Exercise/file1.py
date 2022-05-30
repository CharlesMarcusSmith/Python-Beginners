# Goal: Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.

#The class should have an attribute for the category balance. The class should have methods for withdrawing, depositing and transfering the balance.
class Budget:
    def __init__(self, budget_balance):                                                                                                                                                                 #self creates a unique id, where we call functions below with self, it is telling itself that it is refferring to itself with edits (i think) - it creates unique ID when object created
        self.budget_balance = budget_balance                                                                                                                                                            #setting the variable budget_balance to the input parameters?
    def withdraw_UI(self):                                                                                                                                                                              #successfully retracts from the balance from user input
        withdraw_amount = 0.0
        original_amount = self.budget_balance
        withdraw_amount = input("How much would you like to withdraw?: ")                                                                                                                               #take input from user instead of passing in parameters
        withdraw_amount = float(withdraw_amount)
        self.budget_balance = self.budget_balance - withdraw_amount                                                                                                                                     #written long for ease of reading
        print(f"You have sucessfully withdrawn {withdraw_amount} your new balance is {self.budget_balance}.")
    def transfer(self,d):
        ta = 0.0
        oa = self.budget_balance
        ta = input("Please enter the amount you would like to transfer?: ")
        ta = float(ta)                                                                                                                                                                                 # if ta isnt in the brackets, it reset the value to 0, and the change didnt work, this could be done in the line above
        d.budget_balance = d.budget_balance + ta                                                                                                                                                       #when we print these at the end, the changes have not been made to the balance of the other instance (d) which is names in the parameters when it is called in line 24
       

food_budget = Budget(500.00)
clothing_budget = Budget(500.00)
entertainment_budget = Budget(500.00)


food_budget.transfer(entertainment_budget)
    
    # def deposit(self, amount):
    #     self.budget_balance = self.budget_balance + amount
    #     print(f"You have sucsessfully deposited {ammount} our new balance is {self.budget_balance}.")




print(food_budget.budget_balance)
print(clothing_budget.budget_balance)
print(entertainment_budget.budget_balance)

# def user_choice:
#     input("Which budget would you like to withdraw from? The options are:")


#This ^ should instead all be done by calling functions within instances and parameter trasfering values, not user input