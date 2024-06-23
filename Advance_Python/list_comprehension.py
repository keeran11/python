#what is list Comprehension?
#syantax 1 : normal [expression for variable in iterable]
# nums = [3,6,8,12,14,16]
# sq=[]
# for num in nums:
#     sq.append(num*num)
# print(sq)

# print([num*num for num in nums])

# syntax-2 : if conditon
# [Expession for variable in iterable if cond]
# for num in nums:
#     if num%2==0:
#         sq.append(num*num)
# print(sq)
# print([num*num for num in nums if num%2==0]) #using list comprehension


# syantax -3 : Nested if's
# [Expression for variable in iterable if con1 if cond2]
# for num in nums:
#     if num%2==0:
#         if num%3==0:
#             sq.append(num*num)
# print(sq)
#using list comprehension
# print([num*num for num in nums if num%2==0 if num%3==0])

# syntax -4 If -else
# [Expression if cond else expression for variable in iterable]
# nums = [3,5,6,8,12,14,15]
# result=[]
# for num in nums:
#     if num%2==0:
#         result.append(num*num)
#     else:
#         result.append(num*num*num)
#         print(result)

# print([num*num if num%2==0 else num*num*num for num in nums])

#syntax-5 [expression if cond else expression for var in iterable]
# lst=[]
# for i in range(3,6):
   
#     for j in range(5,7):
    
#         lst.append(i*j)
# print(lst)

# print([i*j for i in range(3,6) for j in range(5,7)])

#Every code cannot be converted into the list comprehension
#adv: compact and elegent code, less code, faster execution dis: less readable


#how to use "if-elif-else"
#chaining: when there is multiple condition we used chaining
# num =int(input("Enter a number:"))
# if num>0:
#     print("Positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

# print("Positive" if num>0 else "negative" if num<0 else "zero")

#another example

# nums = [90,0,-34,33,-21,20]
# status=[]
# for num in nums:
#     if num>0:
#         status.append("Positive")
#     elif num<0:
#         status.append("negative")
#     else:
#         status.append("zero")
# print(status)

# print(["Positive" if num>0 else "negative" if num<0 else "zero" for num in nums])


#checkup fees

checkup_fees=[]
ages=[23,78,16,43,21,17,12,48]
for age in ages:
    if age<18:
        checkup_fees.append(100.0)
    elif age < 30  and age>=18:
        checkup_fees.append(500.0)

    elif age <45 and age>=31:

        checkup_fees.append(700.0)

    else:
        checkup_fees.append(200.0)

print(checkup_fees)
print([100.0 if age<18 else 500.0 if age < 30  and age>=18 else 700.0 if age <45 and age>=31 else 200.0 for age in ages])