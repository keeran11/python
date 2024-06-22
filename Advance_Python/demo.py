# def add(a,b):
#     return a+b

# name = "kiran"

# sports=['cricket', 'kabbaddi', 'tennis', 'badminton']

# enum_obj = enumerate(sports)
# enum_obj = enumerate(sports, start =1) #it start with 1
# print(enum_obj) #create the memory
# print(type(enum_obj)) #it display the type 
# print(list(enum_obj))

#it is mainly used in problem solving in loop
 
# for pos, ele in enumerate(sports, start =1):  #[(pos, ele)]
#     print(f"{pos}: {ele}")


#coversion to dictionary
# print(dict(list(enumerate(sports,1))))  #[(snt,data1),(),()]


#to send the list to the java application or json format and sent to the java applicaton
#best practice is to write in Dict format because json file is in the from of Dic like :keyvalue pairs
import json
sports=['cricket', 'kabbaddi', 'tennis', 'badminton']
data =dict(list(enumerate(sports,1)))
f=open('data.json' , 'w')
json.dump(data,f)
f.close()