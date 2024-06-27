#functional programming ma local identifiers
#scope in programming 
#in programming , the term "Scope" refers to the region of the code where an identifier can be accessed.
#identifier: an identifier is a name using which we can identify a particular object. Object can be 
#variable , function , name, class name etc.

#in Functional programming , there are four types of identifiers.
#1. local identifiers 
#2. global identifiers
#3. non-local identifiers
#4. Built- in indentifiers


#Local identifiers:-

# def display(name):  #this is displsy function
#     age = 22      #variable declearation:local identifiesrs which is inside the function.
#     print(f"{name} has age {age}")
# display("kiran")     #function call

#locals() function
#it helps to identify the variables inside the function
# def display1(name):
#     age = 23
#     x = 20
#     print(f"{name} has age {age}")
#     variables= locals()
#     print(variables)
#     print((variables['x']))

# display1("kiran")

#local variables lai baira bata access garna kojda chai "name error" aauxa
#Global variables:- declare outside the function


country = "nepal" #Global variable

def display():
    name ="kiran" #local varaiables
    print(name)
    country = "india"
    print(f"(your are {name}, you are form {country}") #this access local variables
    

display()
print(f"(your are, you are form {country}")  #this access global variables





