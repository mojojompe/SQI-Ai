class Car: # An object, with multiple functions and properties
    
#properties
    brand = 'toyota'
    model = 'corolla'
    color = 'black'
    
#functions
def start_engine(self):
    return 'Car starting'

my_car = Car() # Separate object using the same model of Class Car, having the same properties
Emma_car = Car()

#my_car()



class Calc:
    brand = None
    color = None
    
    def __init__(self): #Constructor: Whenever the classs is called the init is also called immediately
        self.brand = input("Enter calculator brand: ")
        self.color = input("Enter calculator color: ")
    #Brand and Color can also be defined asin def __init__(self, brand, color):  then self.brand = brand, self.color = color
    #Then while calling the class you can pass the values like Calc('Casio', 'Black')
    
    def on(self):
        print(f'''
              {self.brand} Calculator
              1. Addition
              2. Subtraction
              3. Exit
              ''')
        choice = (input("Enter your choice: "))
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '#':
            print("Exiting...")
            exit()
    
    def Add(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: ")) 
        return a + b
        self.on()

    def Subtract(self):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        return a - b
        self.on()

AwallCalc = Calc()


#Component of OOP
#1. ENCAPSULATION - Wrapping up of data and functions into a single unit (Private, Public, Static, Protected)

class Todo:
    database = []
    name = 'My Todo'
    
    def home(self):
        print(f'''
              Welcome to {self.name} app
              ''')
    def __init__(self):
        pass
    
app = Todo()
app.home()

#adding __ make it private
#adding _ make it protected



#2. INHERITANCE - Deriving properties and functions from a parent class to a child class

class Parent:
    surname = 'Jompe'
    firstname = 'Ade'
    hobby = 'code'
    
    def __init__(self):
        print(f"Hello, my name is {self.firstname} {self.surname}. I love to {self.hobby} ")
        
    def drive (self):
        print(f"{self.firstname} is driving")
parent = Parent()
parent.drive() # prints out the drive function

class Child(Parent): # Child class inheriting from Parent class
    
    def __init__(self): # Overriding the init function of Parent class
       
       self.firstname = 'Tobi' # Overriding the firstname property
       self.hobby = 'play football' # Overriding the hobby property
       super().__init__() # Calling the Parent class init function

child = Child()
child.drive()



#3. POLYMORPHISM - Ability to take many forms (Function Overloading, Operator Overloading, Method Overriding)

