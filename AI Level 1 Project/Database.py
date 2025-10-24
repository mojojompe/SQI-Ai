'''
    BANK APPLICATION PROJECT {Database}
    JOMPE EMMANUEL AYOMIPOSI - 252010
    SQI SOFTWARE ENGINEERING.
    ARTIFICIAL INTELIGENCE.
    Level 1 Python Project
'''


#Connecting the Database

import mysql.connector as sql

connection = sql.connect(
    host = '127.0.0.1',
    port = '3306',
    user = 'root',
    database = 'level_1_project',
    password = ''
)
connection.autocommit = True
mycursor = connection.cursor()

query = 'SHOW DATABASES'

##CREATING DATABASE
#query = 'CREATE DATABASE level_1_project'   


##CREATING THE MAIN CUSTOMER DATABASE TABLE
# query = '''CREATE TABLE customer_list(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     firstname VARCHAR(30),
#     lastname VARCHAR(30),
#     email VARCHAR(50) UNIQUE,
#     account_no VARCHAR(10) UNIQUE,
#     account_bal DECIMAL(10, 2) DEFAULT 0.0,
#     address VARCHAR(50),
#     date_created DATETIME DEFAULT CURRENT_TIMESTAMP
#     )'''



# #TESTING THE TABLE
#query = '''INSERT INTO customer_list(firstname, lastname, email, account_no)
#VALUES('Emmanuel', 'Jompe', 'mojojompe@gmail.com', '3223009490')'''



# #CREATING THE TRANSACTIONS TABLE
# query = '''CREATE TABLE transaction_table(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     sender_email VARCHAR(100),
#     receiver_email VARCHAR(100),
#     amount DECIMAL(10, 2),
#     transaction_type ENUM('deposit', 'withdrawal', 'transfer'),
#     transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (sender_email) REFERENCES customer_list(email),
#     FOREIGN KEY (receiver_email) REFERENCES customer_list(email)
# )'''



# # CREATING THE SAVINGS TABLE
# query = query = '''CREATE TABLE savings_table(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     email VARCHAR(50),
#     target_amount DECIMAL(10, 2),
#     current_amount DECIMAL(10, 2) DEFAULT 0.0,
#     savings_name VARCHAR(100),
#     target_date DATE,
#     created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (email) REFERENCES customer_list(email)
# )'''


# #Forgot to add password in db
# query = 'ALTER TABLE customer_list ADD password VARCHAR(50) AFTER email'
mycursor.execute(query)
print("Table Created Successfully!!")