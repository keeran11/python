# procedural oriented approach where user is added mannually when the
# requirement is added then the code will be increase which is bad approach
# to cover this problem functional programming is came in python.

# one time written code and can be exicute many times which is approach of functional programming.


# def addition(a,b): #function defination
#     print("welcome!")
#     print("addition is ", a + b)

# addition(10, 20)
# addition(11, 202)
# addition(101, 20)

# def addition(a,b): #function defination
#     print("welcome!")
#     print("addition is ", a + b)

# for i in range(2):          #kati samma function run garna ko laagi tyo 2 choti run hunxa
#     a = int(input("Enter first number:"))
#     b = int (input ("Enter Second number:"))
#     addition(a,b)


#reusabilty, write in once and use it more
#two types of function:
#1 : Built in : defined function e.g len() ,

#2 : User-defined: defined by the user

# def function_name([parameters]):
#     staement1   #indentation vaneko enter garepaxi tyaa 4 ota  space hunxa if space vayena vane end hunxa

#There are two types of function :-
#1: parameterized 
#2. non parameterized


# #parameters VS arguments
# def add(a,b):    #parameters
#     print(a+b)

# add(10 , 20) #arguments

# parameters :- formal arguments
# arguments :- actual arguments



#calculation of simple interst:

def simple_intrest(p,t,r):
    print("Principle amount is :", p)
    print("number of years:", t)
    print("rate of interest:", r, "%")
    SI = (p*t*r)/100
    print("Simple interst is :", SI)

simple_intrest(5000,2,12)