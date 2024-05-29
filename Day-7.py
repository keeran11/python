#python loops
#while loops.
count = 1
while count <=5 :
    print("hello")
    count += 1

#next method
i=1
while i <= 5:
    print("hello")
    i+=1

#print number form 1 to 5

i = 1
while i <= 5:
    print(i)
    i += 1

i = 5
while i >= 1:  #loop ma stoping conditon hunxa
    print(i)
    i -= 1

#print number form 1 to 100 using while loop

i = 1
while i <=  100 :
    print(i)
    i += 1

print("loop ended")

# #print number from 100 to 1

i = 100
while i>=1:
    print(i)
    i -=1
print("ended reverse loop")

#print the multiplication table of a number n.

n = int(input("Input the which number you want multipicaion:"))
i = 1
while i<=10:
    print(n*i)
    i += 1


#print the elements of the following list using a loop:
nums = [1,4,9,16,25,36,49,64,81,100]   #list ko member
idx = 0
while idx < len(nums):
    print(nums[idx]) #nums[0] , num[1],...
    idx +=1

    
#search for a number x in this tuple using loop:
#[1,4,9,16,25,36,49,64,81,100]  #tuple huna lai small brackets.


nums=(1,4,9,16,25,36,49,64,81,100)

x = int(input("enter the serach number:"))

i = 0
while i< len(nums):
    if(nums[i] == x):
        print("Found a idx", i)
    else:
        print("finding.")
    i += 1
    


#keywords: Break & continue
i= 1
while i<= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")

i= 0
while i<= 5:
    
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1
print("end of loop")


#odd number
i= 1
while i<= 10:
    
    if(i%2 ==0):
        i += 1
        continue #skip
    print(i)
    i += 1
print("end of loop")


#even number
i= 1
while i<= 10:
    
    if(i%2 != 0):
        i += 1
        continue #skip
    print(i)
    i += 1
print("end of loop")



#loops in pyhton: used fo sequential traveral. for traversing list, string, tuples etc.

nums= [1,3,4,5,6,7]
for val in nums:
    print(val)

tup = (1,3,4,5,6)

for num in tup:
    print(num)



#range() function returns a sequence of numbers, starting form 0 by default. and 
# increments by 1(by default), and stops before a specified numbers.
#range(start? ,stop , step?)
seq = range(5)

for i in seq: #range(5) leykhye ni hunxa

    print(i)


for i in range(2, 10, 2):  #start with 2 upto 10 and step with 2
    print(i)


for i in range(100 , 0 , -1):
    print(i)



#print the multiplication table of a nuber n

n= int(input("enter the number you want to multiply:"))
for i in range(1 , 11):
    print(n*i)


#pass is a null statemnet that does nothing. it is used as a placeholder for future code.




# wap to find the sum of first n numbers(using while) natura number

n = 5
sum = 0
i = 1

while i <= n:
   sum += i
   i += 1
print(sum)

for i in range(n + 1):
   sum += i
print(sum)


#wap to find the factorial of first n numbers .(using for)
n = 3
fact = 1
i = 1

while i <= n:
   fact *= i
   i += 1
print(fact)


n = 5
fact = 1

for i in range(1 , n+1):
      fact *= i
print(fact)