#Regular Expression
#Used for string matching patterns
#Used to search, extract or validate text

import re  #Regex module or check out https://regex101.com


##Email verification using regular expression
# email = input("Email: ")
# pattern = r'^\w+@\w+\.\w+$'
# match = re.match(pattern, email)
# if match:
#     print('Valid Email')
# else:
#     print("Invalid Email")
    


##Other RE functions
pattern = r'\d{3}'
text = 'I have 300 Mangoes and 500 mangoes'
match = re.search(pattern, text)
match = re.findall(pattern, text)
# match = re.sub(pattern, 'some')
print(match)