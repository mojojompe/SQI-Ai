from Bank_Config import BankConfig
class MyBank(BankConfig):
    
    def __init__(self, name):
        super().__init__(name)
        
    def home(self):
        print(f'''Welcome to {self.__BankName}
              1. Deposit
              2. Withdraw
              3. Check Balance
              #. Exit''')