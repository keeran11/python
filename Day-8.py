# to create function 
def func_name(par 1, par 2): paramater = variables

def cal_sum(a,b):
    sum = a+b
    print(sum)
    return sum
cal_sum(1,2)   #function calll
cal_sum(4 ,5)
cal_sum(17 , 5) # we used fucntion to reduce redundancy

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg = (5, 8, 7)


def calc_avg(a=1, b=3, c=10):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg = (5, 8, 7)

def cal_prod(a=4, b=2):
    print(a*b)
    return a*b
cal_prod(8 ,10)

#Waf to print the length of a list(list is the parameter)

cities = ["delhi", "gurgaon", "noida", "pune"]
heros = ["thor", "ironman", "captian america", "shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)


#WAF to print the elemets of a list in a single line(list in the parameter)
cities = ["delhi", "gurgaon", "noida", "pune"]

def print_list(list):
    print(list)

print_list(cities)

def print_list(list):
    for item in list:
        print (item, end=" ")#yesma space diyera output ma ni space aayo 
print_list(cities)
print()

#WAF to find the factorial of n.(n is the parameter)
n = 5

def Cal_fact(n):
    fact =1
    for i in range(1, n+1):
        fact *= i
    print(fact)
Cal_fact(3)


#WAF to convert USD to INR

def converter(usd_val):
    inr_val =usd_val * 83
    print(usd_val, "USD=", inr_val, "INR")
converter(2)

#WAF input the number if the number is odd or even.

def check_odd_even():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

check_odd_even()