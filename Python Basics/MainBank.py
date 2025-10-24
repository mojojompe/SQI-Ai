from BankConfiguration import BankConfig

class MyBank(BankConfig):
    
    def __init__(self, name, db_name, db_pass):
        super().__init__(name, db_name, db_pass)
        
        
        
    def home(self):
        print(f'''
              Welcome to {self.GetBankName()}
              1. Create Account
              2. Login
              #. Exit
              ''')
        choice = input("Choice: ")
        if choice == '1':
            self.register()
        elif choice == '2':
            self.Signin()
        elif choice == '#':
            exit()
        else:
            print("Invalid input!!")
            self.home()
            
            
        
    def register(self):
        fullname = input("fullname: ")
        email = input("email: ")
        password = input("password: ")
        
        result = self.CreateAccount(fullname, email, password)
        message= result['message']
        
        if result['status']:
            print(result['message'])
            self.Signin()
        else:
            print(message)
            self.home()
            
            
            
    def Signin(self):
        print("Login")
        email = input("Email: ")
        password = input("Password: ")
        
        result = self.Login(email, password)
        message = result['message']
        if result['status']:
            print(message)
            print(result['data'])
        else:
            print(message)
            self.Signin()
            
    
    
    def DashBoard(self, user):
        print(f'''
              Welcome back, {user[1]}
              Account No: {user[4]}
              Account Balance: ${user[5]}
              
              1. Deposit
              2. Withdraw
              3. Transfer
              4. Change Password
              5. Create Savings
              6. Transaction History
              7. Home
              ''')
        choice = input("Choice: ")
        if choice == '1':
            self.__Deposit(user[3])  # email is at index 3 in the customer database
        elif choice == '2':
            self.__Withdraw(user[3])
        elif choice == '3':
            self.Transfer(user[3])
        elif choice == '4':
            self.ChangePassword(user[3])
        elif choice == '5':
            self.__CreateSavings(user[3])
        elif choice == '6':
            self.__ShowTransactionHistory(user[3])
        else:
            self.home()
    
    
    def __Deposit(self, email):
        print('Deposit')
        try:
            amount = float(input('Amount: '))
            if amount <= 0:
                print('Amount must be greater than 0')
                self.DashBoard(self.FetchUser(email))
                return
                
            result = self.PerformDeposit(email, amount)
            message = result['message']
            if result['status']:
                print(message)
                user = result['data']
                self.DashBoard(user)
            else:
                print(message)
                self.home()
        except ValueError:
            print('Please enter a valid number')
            self.DashBoard(self.FetchUser(email))
            
        
        
    def __Withdraw(self, email):
        print("Withdraw")
        try:
            amount = float(input('Amount: '))
            if amount <= 0:
                print('Amount must be greater than 0')
                self.DashBoard(self.FetchUser(email))
                return
                
            result = self.PerformWithdrawal(email, amount)
            message = result['message']
            if result['status']:
                print(message)
                user = result['data']
                self.DashBoard(user)
            else:
                print(message)
                self.DashBoard(self.FetchUser(email))
        except ValueError:
            print('Please enter a valid number')
            self.DashBoard(self.FetchUser(email))
        
        
        
    def Transfer(self, email):
        print("Transfer Money")
        try:
            receiver_acct = input("Enter recipient's account number: ")
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0")
                self.DashBoard(self.FetchUser(email))
                return
                
            result = self.PerformTransfer(email, receiver_acct, amount)
            message = result['message']
            
            if result['status']:
                print(message)
                user = result['data']
                self.DashBoard(user)
            else:
                print(message)
                self.DashBoard(self.FetchUser(email))
        except ValueError:
            print("Please enter a valid amount")
            self.DashBoard(self.FetchUser(email))
    
    
    def ChangePassword(self, email):
        print("Change Password")
        old_password = input("Enter current password: ")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        
        if new_password != confirm_password:
            print("New passwords do not match!")
            self.DashBoard(self.FetchUser(email))
            return
            
        result = self.PerformChangePassword(email, old_password, new_password)
        message = result['message']
        
        if result['status']:
            print(message)
            self.home()
        else:
            print(message)
            self.DashBoard(self.FetchUser(email))
            
            
    def __CreateSavings(self, email):
        print("Create New Savings")
        try:
            savings_name = input("Enter savings name/purpose: ")
            target_amount = float(input("Enter target amount: "))
            initial_amount = float(input("Enter initial amount: "))
            target_date = input("Enter target date (YYYY-MM-DD): ")
            
            if initial_amount <= 0 or target_amount <= 0:
                print("Amounts must be greater than 0")
                self.DashBoard(self.FetchUser(email))
                return
                
            result = self.KeepSavings(email, initial_amount, savings_name, target_amount, target_date)
            message = result['message']
            
            print(message)
            self.DashBoard(self.FetchUser(email))
            
        except ValueError:
            print("Please enter valid amounts")
            self.DashBoard(self.FetchUser(email))
            
            
    def __ShowTransactionHistory(self, email):
        print("\nTransaction History")
        print("-" * 50)
        
        result = self.GetTransactionHistory(email)
        if result['status']:
            transactions = result['data']
            for trans in transactions:
                print(f"Type: {trans[0]}")
                print(f"Amount: ${trans[1]}")
                print(f"Description: {trans[2]}")
                print(f"Date: {trans[3]}")
                print("-" * 50)
        else:
            print(result['message'])
            
        input("\nPress Enter to continue...")
        self.DashBoard(self.FetchUser(email))
    
        
    
GTB = MyBank('Gt Bank', 'aipython', '')
GTB.home()