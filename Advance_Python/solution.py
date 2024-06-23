# mylist=[[1,2,3],[4,5,6],[7,8,'a']]
# print("id of mylist:", id(mylist))
# print("id of first element:", id(mylist[0]))
# print("id of second element:", id (mylist[1]))
# print("id of third elemet:", id(mylist[2]))

# newlist =mylist

# print("-" *50)

# print("id of mylist:", id(newlist))
# print("id of first element:", id(newlist[0]))
# print("id of second element:", id (newlist[1]))
# print("id of third elemet:", id(newlist[2]))

# newlist[0][1]=6000   #here 0 is the first one i.e 1,2,3 1 is the second list i.e 4,5,6
# print(mylist)
# print(newlist)

#sometimes you may want to have the original values unchanged and on;y modify the new values
#or vice versa. In python, there are two ways to create copies:

#1) Deep copy
#2) shallow copy

#  - to make these copy work, we use the copy module.
#shallow copy: not good aaproach
import copy

# mylist=[[1,2,3],[4,5,6],[7,8,'a']]
# print("id of mylist:", id(mylist))
# print("id of first element:", id(mylist[0]))
# print("id of second element:", id (mylist[1]))
# print("id of third elemet:", id(mylist[2]))

# newlist =copy.copy(mylist)    #not good approcah but it change the memory of the mylist

# print("-" *50)

# print("id of mylist:", id(newlist))
# print("id of first element:", id(newlist[0]))
# print("id of second element:", id (newlist[1]))
# print("id of third elemet:", id(newlist[2]))

# newlist[2][2]="hello"   #here 0 is the first one i.e 1,2,3 1 is the second list i.e 4,5,6
# print(mylist)


#deep Copy: 

mylist=[[1,2,3],[4,5,6],[7,8,'a']]
print("id of mylist:", id(mylist))
print("id of first element:", id(mylist[0]))
print("id of second element:", id (mylist[1]))
print("id of third elemet:", id(mylist[2]))

newlist =copy.deepcopy(mylist)    #good approcah but it change the memory address of the mylist

print("-" *50)

print("id of mylist:", id(newlist))
print("id of first element:", id(newlist[0]))
print("id of second element:", id (newlist[1]))
print("id of third elemet:", id(newlist[2]))

newlist[2][2]="hello" 
print(newlist)
print(mylist)
