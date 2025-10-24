import datetime as dt

time = dt.datetime.now()
print(time)
print(time.day)
print(time.strftime('%Y'))  #Check the escape codes for other formats
print(time.strptime) #to change strings to datetime format

future = dt.datetime(2026, 3, 24)

next_Birthday = future - time

print(next_Birthday)

user_date = '15/10/25'