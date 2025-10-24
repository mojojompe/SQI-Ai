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
    __connect = None
    __cursor = None
    
    def __init__(self, name, db_name, db_pass):
        self.__BankName = name
        self.__database = db_name
        self.__password = db_pass
        
        self.__connect = sql.connect(
            host = self.__host,
            port = self.__port,
            user = self.__user,
            password = self.__password,
            database = self.__database
        )
        self.__connect.autocommit = True
        self.__cursor = self.__connect.cursor()
        
        
    # def CreateAccount(self, fullname, email, password):
    #     accountNo = randint(1000000000,1099999999)
    #     user = {
    #         "fullname": fullname,
    #         "email": email,
    #         "password": password,
    #         "accountNumber": accountNo,
    #         "Balance": 0.0
    #     }
    #     query = 'INSERT INTO customer_table(fullname, email, password, acct_no) VALUES(%s, %s, %s, %s)'
    #     values = (fullname, email, password, accountNo)
    #     self.__cursor.execute(query, values)
    #     return {
    #         "status": True,
    #         "Message": "Registration Successfull"
    #     }
        
        
    # def Login(self, email, password):
    #     query = 'SELECT * FROM customer_table WHERE email = %s AND password = %s'
    #     values = (email, password)
    #     self.__cursor.execute(query, values)
    #     user = self.__cursor.fetchone()
    #     if user:
    #         return{
    #             "status": True,
    #             "Message": "Login Successful",
    #             "data": user
    #             }
    #     else:
    #         return {
    #         "status": False,
    #         "Message": "Invalid Email and Password!!"
    #         }
        
    # def FetchUser(self, email):
    #     query = 'SELECT acct_bal FROM customer_table WHERE email = %s'
    #     value = (email,)
    #     self.__cursor.execute(query, value)
    #     user = self.__cursor.fetchone()
    #     return user
    
    
    # def UpdateBalance(self, email, balance):
    #     query = 'UPDATE customer_table SET acct_bal =%s WHERE email =%s'
    #     values = (balance, email)
    #     self.__cursor.execute(query, values)
        
        
    # def PerformDeposit(self, email, amount:float):
    #     user = self.FetchUser(email)
    #     if user:
    #         balance = user[0]  # FetchUser returns only acct_bal
    #         new_balance = float(balance) + amount
    #         self.UpdateBalance(email, new_balance)
            
    #         # Get full user data for dashboard display
    #         query = 'SELECT * FROM customer_table WHERE email = %s'
    #         self.__cursor.execute(query, (email,))
    #         updated_user = self.__cursor.fetchone()
            
    #         # Record transaction
    #         query = '''INSERT INTO transaction_table 
    #                   (sender_email, amount, transaction_type)
    #                   VALUES (%s, %s, %s)'''
    #         self.__cursor.execute(query, (email, amount, 'deposit'))
            
    #         return {
    #                 'status': True,
    #                 'message': f'${amount} deposited successfully',
    #                 'data': updated_user
    #         }
    #     else:
    #         return {
    #             'status': False,
    #             'message': f'User not found'
    #         }
        
    
    # def PerformWithdrawal(self, email, amount:float):
    #     user = self.FetchUser(email)
    #     if not user:
    #         return {
    #             'status': False,
    #             'message': 'User not found'
    #         }
        
    #     current_balance = float(user[0])
    #     if current_balance < amount:
    #         return {
    #             'status': False,
    #             'message': 'Insufficient balance'
    #         }
        
    #     # Update balance
    #     new_balance = current_balance - amount
    #     self.UpdateBalance(email, new_balance)
        
    #     # Record transaction
    #     query = '''INSERT INTO transaction_table 
    #               (sender_email, amount, transaction_type)
    #               VALUES (%s, %s, %s)'''
    #     self.__cursor.execute(query, (email, amount, 'withdrawal'))
        
    #     # Get full user data for dashboard display
    #     query = 'SELECT * FROM customer_table WHERE email = %s'
    #     self.__cursor.execute(query, (email,))
    #     updated_user = self.__cursor.fetchone()
        
    #     return {
    #         'status': True,
    #         'message': f'${amount} withdrawn successfully',
    #         'data': updated_user
    #     }
        
        
    # def PerformTransfer(self, sender_email, receiver_acct, amount:float):
    #     # First check if sender exists and has sufficient balance
    #     sender = self.FetchUser(sender_email)
    #     if not sender:
    #         return {
    #             'status': False,
    #             'message': 'Sender account not found'
    #         }
        
    #     sender_balance = float(sender[0])
    #     if sender_balance < amount:
    #         return {
    #             'status': False,
    #             'message': 'Insufficient balance'
    #         }
        
    #     # Find receiver by account number
    #     query = 'SELECT email FROM customer_table WHERE acct_no = %s'
    #     value = (receiver_acct,)
    #     self.__cursor.execute(query, value)
    #     receiver = self.__cursor.fetchone()
        
    #     if not receiver:
    #         return {
    #             'status': False,
    #             'message': 'Receiver account not found'
    #         }
        
    #     receiver_email = receiver[0]
        
    #     # Deduct from sender
    #     new_sender_balance = sender_balance - amount
    #     self.UpdateBalance(sender_email, new_sender_balance)
        
    #     # Add to receiver
    #     receiver_data = self.FetchUser(receiver_email)
    #     receiver_balance = float(receiver_data[0])
    #     new_receiver_balance = receiver_balance + amount
    #     self.UpdateBalance(receiver_email, new_receiver_balance)
        
    #     # Record transaction
    #     query = '''INSERT INTO transaction_table 
    #               (sender_email, receiver_email, amount, transaction_type)
    #               VALUES (%s, %s, %s, %s)'''
    #     self.__cursor.execute(query, (sender_email, receiver_email, amount, 'transfer'))
        
    #     # Get updated sender data
    #     query = 'SELECT * FROM customer_table WHERE email = %s'
    #     self.__cursor.execute(query, (sender_email,))
    #     updated_sender = self.__cursor.fetchone()
        
    #     return {
    #         'status': True,
    #         'message': f'Successfully transferred ${amount} to account {receiver_acct}',
    #         'data': updated_sender
    #     }
    
    
    # def PerformChangePassword(self, email, old_password, new_password):
    #     # Verify old password first
    #     query = 'SELECT * FROM customer_table WHERE email = %s AND password = %s'
    #     values = (email, old_password)
    #     self.__cursor.execute(query, values)
    #     user = self.__cursor.fetchone()
        
    #     if not user:
    #         return {
    #             'status': False,
    #             'message': 'Invalid current password'
    #         }
        
    #     # Update password
    #     query = 'UPDATE customer_table SET password = %s WHERE email = %s'
    #     values = (new_password, email)
    #     self.__cursor.execute(query, values)
        
    #     return {
    #         'status': True,
    #         'message': 'Password changed successfully',
    #         'data': user
    #     }
    
    
    # def KeepSavings(self, email, amount: float, savings_name: str, target_amount: float, target_date: str):
    #     # First check if user has sufficient balance
    #     user = self.FetchUser(email)
    #     if not user:
    #         return {
    #             'status': False,
    #             'message': 'User not found'
    #         }
        
    #     current_balance = float(user[0])
    #     if current_balance < amount:
    #         return {
    #             'status': False,
    #             'message': 'Insufficient balance for savings'
    #         }
        
    #     # Create or update savings
    #     query = '''INSERT INTO savings_table 
    #               (email, target_amount, current_amount, savings_name, target_date)
    #               VALUES (%s, %s, %s, %s, %s)'''
    #     values = (email, target_amount, amount, savings_name, target_date)
    #     self.__cursor.execute(query, values)
        
    #     # Deduct from main balance
    #     new_balance = current_balance - amount
    #     self.UpdateBalance(email, new_balance)
        
    #     # Record transaction
    #     query = '''INSERT INTO transaction_table 
    #               (sender_email, amount, transaction_type)
    #               VALUES (%s, %s, %s)'''
    #     self.__cursor.execute(query, (email, amount, 'withdrawal'))
        
    #     return {
    #         'status': True,
    #         'message': f'Successfully saved ${amount} in {savings_name}'
    #     }
    
    
    # def GetTransactionHistory(self, email):
    #     query = '''SELECT 
    #                 transaction_type,
    #                 amount,
    #                 CASE 
    #                     WHEN transaction_type = 'transfer' AND sender_email = %s THEN CONCAT('Transferred to ', receiver_email)
    #                     WHEN transaction_type = 'transfer' AND receiver_email = %s THEN CONCAT('Received from ', sender_email)
    #                     WHEN transaction_type = 'deposit' THEN 'Deposit'
    #                     WHEN transaction_type = 'withdrawal' THEN 'Withdrawal'
    #                 END as description,
    #                 transaction_date
    #             FROM transactions_table
    #             WHERE sender_email = %s OR receiver_email = %s
    #             ORDER BY transaction_date DESC
    #             LIMIT 10'''
    #     values = (email, email, email, email)
    #     self.__cursor.execute(query, values)
    #     transactions = self.__cursor.fetchall()
        
    #     if not transactions:
    #         return {
    #             'status': False,
    #             'message': 'No transactions found'
    #         }
            
    #     return {
    #         'status': True,
    #         'message': 'Transaction history retrieved successfully',
    #         'data': transactions
    #     }
    
        
    def GetBankName(self):
        return self.__BankName