#\n is used to to break the line.
""" this is the commnet
this is multiline comment in python """

#print("hello \n kiran")

# type thaha pauna ko lagi

"""
x=5
y = "kiran"
print(type(x))
print(type(y))

"""

#variable are container used to store data
#variable can have a short name( like x and y) or a more descriptive name(age,carname, total_volume)
# it should start with letter or underscore
#Create a variable outside of a function, and use it inside the function.
"""
x = "kiran"
def myfunction():
    print(x + " is learning python.")
myfunction()
"""

#python ma k thaha paiyo vane space ko in important hudo raixa.
#function jaha banako ho call handa ni tyesai ko tala raakhna parni rainxa navaye error dido rainxa.
#Create a variable inside a function, with the same name as the global variable.
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is", x)

myfunc()

print("Python is " + x)