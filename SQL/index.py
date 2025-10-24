#Creating a DB for the Bank App

import mysql.connector as sql   #import sql

connect = sql.connect(   # create the connection
    host='127.0.0.1',
    user='root',
    password='',
    port = '3306',
    database = 'aipython'
)

connect.autocommit = True
mycursor = connect.cursor()





#                                                     DDL

query = 'SHOW DATABASES'
#query = 'CREATE DATABASE aipython'

# query = '''CREATE TABLE customer_table(
#         id INT PRIMARY KEY AUTO_INCREMENT,
#         fullname VARCHAR(50),
#         email VARCHAR(50) UNIQUE,
#         acct_no VARCHAR(10) UNIQUE,
#         acct_bal DECIMAL(10, 2) DEFAULT 0.0,
#         address VARCHAR(50),
#         date_created DATETIME DEFAULT CURRENT_TIMESTAMP
        
#         )'''

# query = 'ALTER TABLE customer_table ADD password VARCHAR(50) AFTER email'

#query = 'ALTER TABLE customer_table CHANGE acct_bal account_bal' 

# DROP and TRUNCATE are also functions





#                                                      DML

# query = '''INSERT INTO customer_table(fullname, email, password, acct_no)
# VALUES('Emmanuel Jompe', 'mojojompe@gmail.com', '2007', '3223009490' )'''

# query = '''INSERT INTO customer_table(fullname, email, password, acct_no)
# VALUES(%s, %s, %s, %s)'''

# values = ('Mojo Jompe', 'jompe@gmail.com', '2007', '0857729344')

# query = '''UPDATE customer_table SET fullname = %s WHERE id = %s'''
# values = ('Jompe Emmanuel', 3)

# query = 'DELETE FROM customer_table WHERE id = 3'





#                                                        DQL

# query = 'SELECT * FROM customer_table'     #To get all users in table
# mycursor.execute(query)
# details = mycursor.fetchall()
# print(details)


# query = 'SELECT * FROM customer_table WHERE id = 1'   #To get a single user
# mycursor.execute(query)
# details = mycursor.fetchone()
# print(details[2], details[3], details[4])


# query = 'SELECT fullname, email, acct_no, acct_bal FROM customer_table WHERE email =%s AND password =%s'
# email = input('Email: ')
# password = input('Password: ')
# values = (email, password)
# mycursor.execute(query, values)
# details = mycursor.fetchone()
# if details:
#     print('Login Successful')
# else:
#     print('Invalid Email or Password')


# # Create transactions table
# query = '''CREATE TABLE transaction_table(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     sender_email VARCHAR(50),
#     receiver_email VARCHAR(50),
#     amount DECIMAL(10, 2),
#     transaction_type ENUM('deposit', 'withdrawal', 'transfer'),
#     transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (sender_email) REFERENCES customer_table(email),
#     FOREIGN KEY (receiver_email) REFERENCES customer_table(email)
# )'''
# mycursor.execute(query)

# # Create savings table
# query = '''CREATE TABLE IF NOT EXISTS savings_table(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     email VARCHAR(50),
#     target_amount DECIMAL(10, 2),
#     current_amount DECIMAL(10, 2) DEFAULT 0.0,
#     savings_name VARCHAR(100),
#     target_date DATE,
#     created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (email) REFERENCES customer_table(email)
# )'''

#query = 'DROP TABLE transactions_table'
mycursor.execute(query)

print("Tables created successfully")