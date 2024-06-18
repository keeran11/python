#to print the percentage of the student.

class Student:
    def __init__(self, phy, chem, math):
        self.phy =phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97 , 99)
# print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
# print(stu1.percentage)      # yeha student ko physic ko marks change garda % change vayena

stu1.calcPercentage()
print(stu1.percentage)



#here is this is one method of dowing 

# yo lai aajai better tarikale garani garna sakinxa i.e decorator ie @property
#we use @proerty decorator on any method in the class to use the method as property.
class Student:
    def __init__(self, phy, chem, math):
        self.phy =phy
        self.chem = chem
        self.math = math
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) /3) +"%"

stu1 = Student(98, 97 , 99)
# print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)


#Ploymorphism: Operator Overloading
#when the same operator is alowed to have deffernt meaning according to the context.
class Complex:
    def __init__(self, real, img):   #defination of constracotr
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")
num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(4, 6)
num2.showNumber()

num3= num1.add(num2)
num3.showNumber()



#adding complex number

class Complex:
    def __init__(self, real, img):   #defination of constracotr
        self.real = real
        self.img = img
    
    def showNumber(self):
        # print(self.real, "i +", self.img, "j")
        print(f"{self.real}i + {self.img}j")
    def __add__(self, num2):            #dunder function which can add ie __add__
    # def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

# # Create instances of Complex class   
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

# Add num1 and num2
num3 = num1 + num2
# num3= num1.add(num2)
num3.showNumber()


#define a Circle class to create a circle with radius r using the constructor.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius **2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
        
        

c1 = Circle(5)
print(c1.Area())
print(c1.perimeter())


    

#define an Area() method of the class which calculate the area of the circle.
#Define a Perimeter() method of the class whih allows you to calculate the perimeter of the circle.




#Define a Employee class with attributes role, department &salary. this 
#Create an Engineer class that inherits properties from Emoloyee & 

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("role = ", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age= age
        super().__init__("Engineer", "IT", "75,000")

engg1= Engineer("Kiran Kumar Acharya", 26)
engg1.showDetails()

e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()


#Create a class called Order which stores itsm & its price.
#Use Dunder function __gt__() to convey that:
#order1> order2> if price of order1> price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

oder1 = Order("chips",20)
order2 = Order("tea", 15)
print(oder1 > order2)
