#ERRORS
# 1. Runtime Error ~ Errors seen when file is run
# 2. Compile Time Error ~ Errors seen when 


# Try
# except
# else
# finally

# nums = range(20)
# try:
#     x = (nums[10])
# except:
#     print('An error occured')
# else: #works when no error occurs
#     print(x)
    
# finally:
#     print('I run if there is an error or not')



nums = [1,2,3,4]
try:
    print(nums[1])
    print(2/10)
except IndexError as i:
    print(f'Error: {i}')
except NameError as n:
    print(f'Error: {n}')
except Exception as e:
    print(f'Error: {e}')