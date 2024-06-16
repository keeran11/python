#private(like)attribues & methods
#private attributes & methods are meant to be used only within the class and are not accessible
#outside the class.
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass= acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
    
acc1 = Account('12345', "abcde")
print(acc1.acc_no)
print(acc1.reset_pass())

#Private(like) attributes & methods
#Conceptual implementations in python
#Private attributes & methods are meant to be used only within the class and are not
#ACCESSIBLE FROM outside the class.

class Person:
    __name ="anonymous"

    def __hello():
        print("hello person")
p1 = Person()
print(p1.__hello())


#Inheritance:
#when one class(childderived) derives the properties & methods of another class(parent/base)
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toytacar(Car):
    def __init__(self,name):
        self.name = name

car1 = Toytacar("fortuner")
car2 = Toytacar("prius")

print(car1.color)


#inheritance types:
# 1 single
# 2 multi-level
# 3 multiple 

#2 multi- level inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class Toytacar(Car):
    def __init__(self,name):
        self.name = name

class Fortuner(Toytacar):
    def __init__(self, type):
        self.type = type

car1 = Toytacar("fortuner")
car2 = Fortuner("diesel")
car2.start()

#Multiple Inheritance
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A , B):
    varC= "welcome to class C"
c1 =C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#super method
#super() method is used to access methods of the parent class
class Car:
    def __init__(self,type):  #created constractor
        self.type = type

    @staticmethod
    def start():
        print("car started")
    def stop():
        print("car stopped")

class ToyotaCar(Car):            #properties
    def __init__(self, name, type):
        super().__init__(type)
        self.name= name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)

#class method
# A class method is bound to the class & recieves the class as an implicit first argument.
#Note- Static method can't access or modify class state & generally for utility.

class Student:
    @classmethod        #decorator
    def college(cls):
        pass
