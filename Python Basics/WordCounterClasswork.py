#Word Counter Classwork.

word = str(input("Enter your Words: ")).split(" ") #splits the entire writeup into words
count = len(word) #Counts the already splitted words

print(f"You have {count} words in this write-up")
