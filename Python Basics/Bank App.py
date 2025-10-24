#Using the Basic OOP logic


class Bank:
    __balance =   0 #private var
    __BankName = None  #private var
    
    def __init__(self, name):
        
        
        self.__BankName = name
        
    def home(self):
        print(f'''Welcome to {self.__BankName}
              1. Deposit
              2. Withdraw
              3. Check Balance
              #. Exit''')
        
        Choice = input('Enter your choice: ')
        if Choice == '1':
            self.Deposit()
        elif Choice == '2':
            self.Withdraw()
        elif Choice == '3':
            self.CheckBalance()
        elif Choice == '#':
            print("Bye...")
            exit()
        else:
            print("Invalid Input!!")
            self.home()
            
            
            
    def CheckBalance(self):
        print (f"Your Balance is {self.__balance}") 
        self.home() #run bk.CheckBalance to see
        
        
        
    def Deposit(self):
        amount = float(input("Enter Amount: "))
        if amount < 1:
            print("Invalid Input!!")
        else:
            self.__balance += amount
        print("Deposit Successful")
        self.home()
        
        
        
    def Withdraw(self):
        amount = float(input("Enter Amount: "))
        if amount < 1:
            print("Invalid Input!!")
        elif amount > self.__balance:
            print('Insufficient Funds')
        else:
            self.__balance -= amount
        print("Withdrawal Successful")
        self.home()
        
    
            
bk = Bank('First Bank')
#bk.__BankName = 'Polaris', Not possible because the bank name is protected
bk.home()

        
#Modularisation
# 1. Scripts - A file with python code with extension '.py' 
# 2. Module - More than one script
# 3. Library - Collection of Modules and packages (folder of folders)
# 4. Framework - Tools that simplify or accelerate a development process


from config.Bank_Config import shout #Modularization

import random 
import time

import pyttsx3
sound = pyttsx3.init()
