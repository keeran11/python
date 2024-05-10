# String is data type that stores a sequence of data


str1 = "This is a string. \n Hi my name is kiran"
Str2 =' this is also string'
str3 = """this is a string"""
print(str1)


# escape sequence character 
# concatenation: process of adding two string we use + operator of adding two string.



print(str1 + str3)


len(str) here len is the function which is used to calculate the length of the string


len = len(str3)
print(len)



# length ma space and special character count hunxa

# indexing




str = "kiran acharya"

print(str[3])


slicing: accessing parts of  a string

print(str[: 3])
print(str[3 : ])
print(str[2: 6])
 
 negative index A P P L E [ a= -5 , p = -4 , p = -3 , l= -2 E= -1]



print(str[-3 : -1])  #yes ma output chai 'ry' aauxa ra last ko -1 ma raheko 'a' chai escape hunxa

# functio stings


print(str.endswith("ya")) #it check weacther it end with last letter ya or not?

print(str.capitalize())

replace functon

print(str.replace ("kiran" , "janak"))


print(str.find("acharya"))


print(str.count("a"))



# program:1 web to input user's first name & print its length.

name = input("Enter your name:", )
print( "The length of my name is :" ,len(name))




# wap to find the occurance of $ in a string.

str = "kiran love $"
print(str.find("$"))



conditional statements : if - elif - else(syntax)  indentation: is the proper space ,it is important in the python
light = "none"
if(light =="red"):
    print("stop ")
elif(light == "green"):
    print("go")

elif(light=="yellow"):
    print("watch and go")
else:
    print("light is broken")



#grade sheet print:


marks = int(input("Enter the Marks of the student:"))

if(marks >=90):
    grade = "A"
elif(marks >=75 and marks <90):
    grade = "B"
elif(marks >=60 and marks < 75):
    grade = "C"
elif(marks >=45 and marks <56):
    grade = "D"
else:
    print("your are fail")
str(print("Your grade of your exam is :" , grade))




# nesting: yek statement ko vitra aarko statement

# WAP to check if a number entered by the user is odd or even.

num= int(input("Please Enter  the Number:"))
rem = num % 2


if (rem == 0):
    print("The entered number is even")
else:
    print("The number is odd")



# wap to find the greatest of 3 number entered by the user.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if (num1 >= num2 and num1 >= num3):
    print("num1 is the greatest number:",num1)
elif (num2 >= num3) :
    print("num2 is the greatest number:", num2)
else:
    print("the num3 is the greatest number:",num3)


# wap to check if a number is a multiple of 7 or not.

num = int(input("Enter the number to check wheater the number is multiple of 7 or not:"))

if (num % 7 == 0):
    print("this number is multiple of 7")
else:
    print("this number is not multiple of 7")
