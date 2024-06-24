#dictionary comprehension in python


# nums= [1,2,3,4,5]
# my_dict={}
# for num in nums:
#     if num%2==0:
#         my_dict [num]=num **2

# print(my_dict)

# print({num:num**2 for num in nums})
# print({num:num**2 for num in nums if num%2==0})


#ex2
# str1 = "cOding"
# my_dict ={}
# for char in str1:
#     my_dict[char.upper()]= (ord(char), ord(char.swapcase()))  #ord is ascii of C, 
# print(my_dict)


# print({char.upper():(ord(char), ord(char.swapcase())) for char in str1})


#ex3 set comprehension

nums=[1,2,3,4]

print({n**2 for n in nums})  #set is unordered  datastructure which do not maintain the order of output.
#dublicate is not allowed in sets

