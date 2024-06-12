#OOP in python: to map with real world scenarios, we started using objects in code.
#this is called object oriented programming.
#we use OOP to decrease refundancy and incerase reusability.

#class is a blueprint for creating objects.

#creating class
class Student:          #generally while creating the class we start with caital letter.
    name ="Kiran Kumar Acharya"

#creating object(instance)

s1 = Student()
print(s1.name)



#__init__ function
#Constructor , all classes have a function called __init__(), which is always executed
# when the class is being initiated.

# creating class
class Student:
    def __init__(self, fullname , marks):
        self.name = fullname
        self.marks = marks

# #creating object

s1 = Student ("kiran Kumar Acharya", 97)
print(s1.name, s1.marks)

#the self parameter is a reference to the current instance of the class, and is used to
#access variables that belongs to the class.
#attributes --> data, variables.


#default constructors
def __init__ (self):  #only 1 parameter that is self by default python will create default constutors
    pass

#parameterized constructors

def __init__(self ,name , marks):   # more then one parameter
    self.name = name
    self.marks =marks
    print("adding new student in Database..")



#attributes
#class & instance attributes
# Class.attr
# Object.attr 

#methods: Methods are functions that belong to objects.

#Create student calss that takes name & marks Of 3 subjects as arguments in constructor
#then create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)
s1 = Student("tony stark", [99, 98,97])
s1.get_avg()
