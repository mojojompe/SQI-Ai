'''
    BANK APPLICATION PROJECT
    JOMPE EMMANUEL AYOMIPOSI - 252010
    SQI SOFTWARE ENGINEERING.
    ARTIFICIAL INTELIGENCE.
    Level 1 Python Project
'''


#The Configuration or 'Backend' for the Bank App

from random import randint
import mysql.connector as sql

class BankConfig:
    __BankName = None
    __host = '127.0.0.1'
    __port = '3306'
    __user='root'
    __password= ''
    __port = '3306'
    __database = None
    __connection = None
    __cursor = None
    
    
    
    def __init__(self, name, db_name, db_pass):
        self.__BankName = name
        self.__database = db_name
        self.__password = db_pass
        self.__connection = sql.connect(
            host = self.__host,
            port = self.__port,
            user = self.__user,
            password = self.__password,
            database = self.__database,
        )
        self.__connection.autocommit = True
        self.__cursor = self.__connection.cursor()
    
    
    
    #Function to get all users
    def FetchUser(self, email):
        query = 'SELECT * FROM customer_list WHERE email = %s'
        value = (email,)
        self.__cursor.execute(query, value)
        user = self.__cursor.fetchone()
        return user
    
    
    
    # Function to Create a new account
    def CreateAccount(self, firstname, lastname, email, password, address):
       #To create special account number for each user
        account_no = randint(1000000000,1099999999)
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "account_no": account_no,
            "account_bal": 0.0,
            "address": address
        }
        query = 'INSERT INTO customer_list(firstname, lastname, email, password, account_no, address) VALUES(%s, %s, %s, %s, %s, %s)'
        values = (firstname, lastname, email, password, account_no, address)
        self.__cursor.execute(query, values)
        return{
            "status": True,
            "message": "Registration Successful"
        }
        
        
        
    #Function to Login
    def Login(self, email, password):
        query = 'SELECT * FROM customer_list WHERE email = %s AND password = %s'
        values = (email, password)
        self.__cursor.execute(query, values)
        user = self.__cursor.fetchone()
        if user:
            return{
                "status": True,
                "message": "Login Successful",
                "data": user
            }
        else: 
            return{
                "status": False,
                "message": "Invalid Email and Password!"
            }
            
            
            
    #Function to Change Password
    def PerformChangePassword(self, email, old_password, new_password):
        #Confirm old password
        query = 'SELECT * FROM customer_list WHERE email = %s AND password = %s'
        values = (email, old_password)
        self.__cursor.execute(query, values)
        user = self.__cursor.fetchone()
        
        if not user:
            return {
                'status': False,
                'message': 'Invalid password, cannot make change for security'
            }
        #Change password if previous matches
        query = 'UPDATE customer_list SET password = %s WHERE email = %s'
        values = (new_password, email)
        self.__cursor.execute(query, values)
        return {
            'status': True,
            'message': 'Password successfully changed',
            'data': user
        }
                                
        
        
    #Function to Perform Deposit
    def PerformDeposit(self, email, amount:float):
        user = self.FetchUser(email)
        if user:
            balance = user[6]  # account_bal is at index 6
            new_balance = float(balance) + amount
            self.UpdateBalance(email, new_balance)
            
            # Record transaction in Transaction History Table 
            query = '''INSERT INTO transaction_table 
                      (sender_email, amount, transaction_type)
                      VALUES (%s, %s, %s)'''
            self.__cursor.execute(query, (email, amount, 'deposit'))
            
            # Get updated user data
            query = 'SELECT * FROM customer_list WHERE email = %s'
            self.__cursor.execute(query, (email,))
            updated_user = self.__cursor.fetchone()
            
            return {
                    'status': True,
                    'message': f'${amount} deposited successfully',
                    'data': updated_user
            }
        else:
            return {
            'status': False,
            'message': f'User not found',
            }
            
            
            
    #Function to Update Balance after deposit or transfer
    def UpdateBalance(self, email, balance):
        query = 'UPDATE customer_list SET account_bal =%s WHERE email =%s'
        values = (balance, email)
        self.__cursor.execute(query, values)
        
     
        
    #Function to perform withdrawal
    def PerformWithdrawal(self, email, amount:float):
        user = self.FetchUser(email)
        if not user:
            return{
                'status': False,
                'message': 'User not found'
            }
            
        current_balance = float(user[6])  # account_bal is at index 6
        if current_balance < amount:
            return{
                'status': False,
                'message': 'Insufficient Funds'
            }
        #Updating balance after withdrawal
        new_balance = current_balance - amount
        self.UpdateBalance(email, new_balance)
        
        #To record transaction in Transaction History Table
        query = '''INSERT INTO transaction_table(
            sender_email, amount, transaction_type)
            VALUES (%s, %s, %s)'''
        self.__cursor.execute(query, (email, amount, 'Withdrawal'))
        
        #To get full updated user data for display
        query = 'SELECT * FROM customer_list WHERE email = %s'
        self.__cursor.execute(query, (email,))
        updated_user = self.__cursor.fetchone()
        
        return {
            'status': True,
            'message': f'${amount} withdrawn successfully',
            'data': updated_user
        }
        
        
        
    #Function to Perform Transfer to another user
    def PerformTransfer(self, sender_email, receiver_acct, amount:float):
       
        #Confirm if user exists and has enough balance
        sender = self.FetchUser(sender_email)
        if not sender:
            return {
                'status': False,
                'message': 'Sender account not found'
            }
            
        sender_balance = float(sender[6])
        if sender_balance < amount:
            return {
                'status': False,
                'message': 'Insufficient balance'
            }
        #To find receiver by account number
        query = 'SELECT email FROM customer_list WHERE account_no = %s'
        value = (receiver_acct,)
        self.__cursor.execute(query, value)
        receiver = self.__cursor.fetchone()
        
        if not receiver:
            return {
                'status': False,
                'message': 'Receiver Account not found'
            }
        receiver_email = receiver[0]  # email is the only field we selected in the query
        
        #To deduct from sender after transaction
        new_sender_balance = sender_balance - amount
        self.UpdateBalance(sender_email, new_sender_balance)
        
        #Adding to receiver after debiting sender
        receiver_info = self.FetchUser(receiver_email)
        receiver_balance = float(receiver_info[6])
        new_receiver_balance = receiver_balance + amount
        self.UpdateBalance(receiver_email, new_receiver_balance)
        
        #Recording the transaction in Transaction History
        query = '''INSERT INTO transaction_table(
            sender_email, receiver_email, amount, transaction_type)
            VALUES(%s, %s, %s, %s)'''
        self.__cursor.execute(query, (sender_email, receiver_email, amount, 'Transfer'))
        
        #Update sender data
        query = 'SELECT * FROM customer_list WHERE email = %s'
        self.__cursor.execute(query, (sender_email,))
        updated_sender = self.__cursor.fetchone()
        
        return {
            'status': True,
            'message': f'Successfully transferred ${amount} to account {receiver_acct}',
            'data': updated_sender
        }
        
        
        
    #Function to show all Transactions
    def GetTransactionHistory(self, email):
        query = '''SELECT 
                    transaction_type, 
                    amount, 
                    CASE
                        WHEN transaction_type = 'transfer' AND sender_email = %s THEN CONCAT('Transferred to ', receiver_email)
                        WHEN transaction_type = 'transfer' AND receiver_email = %s THEN CONCAT('Received from ', sender_email)
                        WHEN transaction_type = 'deposit' THEN 'Deposit'
                        WHEN transaction_type = 'withdrawal' THEN 'Withdrawal'
                    END as description,
                    transaction_date
                FROM transaction_table
                WHERE sender_email = %s OR receiver_email = %s
                ORDER BY transaction_date DESC
                LIMIT 10'''
        values = (email, email, email, email)
        self.__cursor.execute(query, values)
        transactions = self.__cursor.fetchall()
        
        if not transactions:
            return{
                'status': False,
                'message': 'No Transactions Found'
            }
            
        return{
            'status': True,
            'message': 'Transaction History retrieved successfully',
            'data': transactions
        }
    
    
    
    
    #Function to Keep Savings
    def KeepSavings(self, email, amount: float, savings_name: str, target_amount: float, target_date: str):
        #Check if acount balance is enough
        user = self.FetchUser(email)
        if not user:
            return{
                'status': False,
                'message': 'User not found'
            }
        
        current_balance = float(user[6])
        if current_balance < amount:
            return{
                'status': False,
                'message': 'Insufficient Balance for saving'
            }
            
        #To Save in savings table
        query = '''INSERT INTO savings_table
                (email, target_amount, current_amount, savings_name, target_date)
                VALUES (%s, %s, %s, %s, %s)'''
        values = (email, target_amount, amount, savings_name, target_date)
        self.__cursor.execute(query, values)
        
        #To remove savings from account
        new_balance = current_balance - amount
        self.UpdateBalance(email, new_balance)
        
        #Recording the transaction in Transaction history
        query = '''INSERT INTO transaction_table 
                (sender_email, amount, transaction_type)
                VALUES (%s, %s, %s)'''
        self.__cursor.execute(query, (email, amount, 'withdrawal'))
        return{
            'status': True,
            'message': f'{amount} successfully saved in {savings_name}'
        }
        
        
        
        
    def GetBankName(self):
        return self.__BankName
    