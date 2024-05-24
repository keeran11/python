# dictonary in python: is used to store data values in key:values pairs, they are unordered, mutable, don't allow duplicate keys.

# dict = {
#     "key" : "value",
#     "name" : "kiran",
#     "subjects" : ["python", "c", "java"],
#     "topic": ("dict", "set"),
#     "learning" : "coding",
#     "age" : "26"
# }
# print(dict["key"])
# print(dict["subjects"])
# dict["name"] = "raj"
# print(dict["name"])

# nested dictionaries: dictonary ko vitra fyeri aarko dict raakhyo vane tyo lai nested dictnories vaninxa

# Student = {
#     "Name" : "Kiran Kumar Acharya",
#     "Subject": {
#         "math" : 98,
#         "science" : 78,
#         "english" : 26,
#         "Nepali": 78,
#     }
# }

# print(Student["Subject"])
# print(Student["Subject"]["science"])


# dictonary methods:

# Student = {
#     "Name" : "Kiran Kumar Acharya",
#     "Subject": {
#         "math" : 98,
#         "science" : 78,
#         "english" : 26,
#         "Nepali": 78,
#     }
# }
# # print(Student.keys())   #here output ma chai dictionary ma kun kun keys haru xa vanni print garxa like: Nmae and subject
# # print(Student.values()) #yo le chai yo key ma kun kun value xa vanni print garxa
# # print(Student.items())  #yo le chai yo dict ma keys ra value duetai print garxa
# print(list(Student.items()))    #yo le chai tuple ko form ma list gardinxa
# print(Student.get("Name"))
# Student.update({"city" : "kathmandu"})  #this will update in dictionary
# print(Student)



# python Sets:
# collection = { 1 , 2 , 3}
# print(collection.pop())

#store following word meaning in a python dictionary:
#table : "a piece of furniture", "list of facts & figures"
# "a small animal"

# dictonary = { 
#     "cat" : "a small animal",
#     "table" : ["a piece of funicture","list of facts & figures"]
# }

# print(dictonary)


#you are given a list of subjects for students. Assume one classroom is required for 1 subject. how many classrooms are needed by all students.
#"python", "java", "C++" , "pyhon", "javascripts",
#"java" ," python", "java", "C++", "C"

# subjects = {
#     "python" , "java", "c++", "python", "javascripts", "java",
#     "python", "java", "c++", "c"
# }
# print(subjects)
# print(len(subjects))

#WAP to enter marks of 3 subjects form the user and store them in a dictionary. start with empty dictionary
#and add one by one. USE Subjects name as key & marks as value.

grade = {

}
x =int(input(" enter the marks of math:"))
grade.update({"math" : x})
y = int(input(" enter the marks of physic:"))
grade.update({"Physic": y})
z =int(input(" enter the marks of python:"))
grade.update({"python" : z})
print(grade)


#figure out a way to store 9 & 9.0 as separate values in the set (you can take help of built-in data types)
