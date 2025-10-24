name = input("Enter your name: ")

score = float(input("Enter your score: "))

if score in range(70,101):
    print(f"Congratulations {name}, your grade is A")
    
elif score in range(60,70):
    print(f"Good Job {name}, your grade is B")
    
elif score in range(50,60):
    print(f"Welldone {name}, your grade is C")

elif score in range(45,50):
    print(f"Keep trying {name}, your grade is D")

elif score in range(40,45):
    print(f"Better Luck Next time {name}, your grade is E")
    
elif score in range(0,40):
    print(f"Give up {name}, your grade is F")