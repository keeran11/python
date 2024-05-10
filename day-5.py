# list and tuples
# built in data types that store set of values.it is denoted by big brackets []

marks = [87 , 80 , 90, 70]
print(marks)
print(len(marks))
print(type(marks))
print(marks.append(4))
print(marks)


# list ko dur ko vai, which is used to create immutable sequence of vaules.
# single value to last ma , launa chai paarxa

tuple = (2 , 5 , 6, 2)
print(type(tuple))

# methods in tuples ie index(el) tup .count

print(tuple.index(2))
print(tuple.count(2))

# WAP to ask the user to enter names of their 3 favourate movies & store them in a list.
movies = []
mov1 = input("Enter the name of your first movies:")
mov2 = input("Enter the name of your second movies:")
mov3 = input("Enter the name of your third movies:")
movies.append(mov1)
movies.append(mov2)


movies.append(mov3)



movies.append(input("enter the name of the forth movie:"))
print(movies)


# Wap to check if a list contains a palindrome of elements. (hint: use copy() method)
# palindrome vaneko suru bata padeni last bata padeni tyo same huni lai vanixa eg: maam

list1 = [1 ,2 ,3 ,2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 ==list1):
    print("the number is palindrome number")
else:
    print("the given number is not a palindrome number")


# WAP to count the number of studnent with the "A " grade in the following tuple ["C" , "D " "A" ,"B " "B " "A"]


grade = ("C" , "D " ,"A" ,"B " ,"B ", "A")
print(grade.count("A"))

# WAP the above values in a list & sort them "A "to "D"

grade = ["C" , "D " ,"A" ,"B " ,"B ", "A"]
grade.sort()
print(grade)