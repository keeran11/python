#Static methods
#Methods that don't use the self parameter(work at class level)

# class Student:
#     @staticmethod  #decorator:allows us to wrap another functon in order  to extend the behaviour of the wrapped function, without permanently modifying it.

#     def college():
#         print("ABC College")



#Abstraction: hiding the implementing details of a class and only showing the essential features to the user.
#Encapusalation: wrapping data and functions into a single unit objects.

#create Account class with2 attrbutes - balance & account no.

class Account:
    def __init__(self, bal, acc):  #construcor defined
        self.balance = bal
        self.account_no = acc

acc1 = Account(100000, "pr0051275")
print("your balance is :",acc1.balance)
print("Your account number is : ",acc1.account_no)


#create method for debit, credit &printing the balance.
class Account:
    def __init__(self, bal, acc):  #construcor defined
        self.balance = bal
        self.account_no = acc

        #debit method

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = " , self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs." , amount , "was credited")   
        print("Total balance = " , self.get_balance())  

    def get_balance(self):
        return self.balance      

        
acc1 = Account(100000, "pr0051275")
print("your balance is :",acc1.balance)
print("Your account number is : ",acc1.account_no)
acc1.debit(2000)
acc1.credit(20)
