# Updated CBT Application Assignment
'''This updates has the following additions
1. Prompt asking for the amount of students and registering them.
2. Calling out each student for their examination based on their registeration numbers.
3. Printing out the students with the highest and lowest scores
4. Printing out the Average score
'''


#Code
print("\tSQI COLLEGE OF ICT")
print("DEPARTMENT OF SOFTWARE ENGINEERING")
print("ARTIFICIAL INTELLIGENCE PYTHON EXAMINATION")

Students = []
Mat_Nos = []
Scores = []


#Registration
print("NOTE: This is for Examiners only!!")
AmountOfStudents = int(input("How many students are offering this examination?: "))
for i in range(1,AmountOfStudents+1):
    name = input(f"Enter student {i}'s name: ").strip()
    mat_No = input(f"Enter student {i}'s Matric Number, eg. SAI01: ").lower().strip()
    score = 0
    if "sai" not in mat_No:
        print(f"Enter a valid Matric Number!")
        break
    else:
        Students.append(name)
        Mat_Nos.append(mat_No)
        Scores.append(score)

if i == AmountOfStudents:
    print("Students Registered successfully!!")
All = list(zip(Students, Mat_Nos, Scores))


#Examination, one by one
Questions = ['1. What is the way to display a string in Python:\n a. System.out.println(string)\n b. disp("String")\n c. print(string)\n d. print("string")',
             '2. What data type is used to store text in Python\n a. str\n b. int\n c. bool\n d. arr', 
             '3. What keyword is used to define a function in Python: \n a. void ()\n b. int main() \n c. def\n d. const => ()',
             '4. Is Python an OOP language: \n a. You dey Whine?\n b. Yes\n c. No\n d. I think so',
             '5. What is Artificial Intelligence? \n a. Ironmans Jarvis \n b. Android in MIB \n c. Terminator\n d. Robots and Machines, thinking like humans']
Answers = ['d', 'a', 'c', 'b', 'd']

MarkingScheme = list(zip(Questions, Answers))

print(" ")
start = input("Are the students ready for the Exams? Yes or No: ").lower().strip()
if start == "yes":
    print("The Examination is accordingly to the Register")
    
    for name, mat_No, score, in All:
        print(" ")
        print(f"Welcome {name}, would you like to proceed with your exam? ")
        print(" ")
        proceed = input("\tEnter Yes or No to proceed: ").lower()
        if proceed == "yes":
            print(" ")
            print("\tThe Examination is 100 marks, Goodluck!")
            print(" ")
            print("Choose only the option")
            print(" ")
            for k in range(len(Questions)):
                print(Questions[k])
                Ans = input("Your answer: ").lower().strip()
                if Ans == Answers[k]:
                    score += 20            
            print(" ")
            print(f"Congratulations {name}, you scored {score}/100 in your Exam.")
        else:
            Scores.append(0)
            print(" ")
            print("Alright then, You don't want to write the exam. Bye!")
        Scores.append(score)
else:
    print("Bye for now!!")
    
    
#Results and Examination Statistics

print(" ")
print(" ")
print(" ")
print("Examination Results for all Students")
print(" ")
for x in range (len(Students)):
    print(f"{Students[x]} with Matric Number, ({Mat_Nos[x]}) scored: {Scores[x]} marks")
    
#Statistics
HighestScore = max(Scores)
LowestScore = min(Scores)
AverageScore = sum(Scores) / len(Scores)

print(" ")
print(" ")
print(f"The Highest score is {HighestScore}")
print(" ")
print(f"The Lowest score is {LowestScore}")
print(" ")
print(f"The Average score of all students is {AverageScore}")
print("Bye.")
print(" ")

