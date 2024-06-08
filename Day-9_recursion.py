#Recursion is a functon calls itself repeatedly
#loops and recursion is interrelated.
# def show(n):
#     if (n == 0): #base case which decide where the recursion when to stop.  
#         return
#     print(n)
#     show(n-1)
# show(5)
    


#returns n!
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(2))

#write a recursive function to calculate the sum of first n natural numbers.

# def cal_sum(n):
#     if (n == 0): #base case chai chainxa hai 
#         return  0
#     return cal_sum(n-1)+ n
# print(cal_sum(5))

#write a recursive fuction to print all elemet in a list.
#hint: use list & index as parameters.


def print_list(list, idx= 0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits =["mango", "litchi", "apple", "banana", "dragon fruits"]

print_list(fruits)