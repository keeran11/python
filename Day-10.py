#file I/O in python
#python can be used to perfoerm operation on a file(read & write date)

# f = open ("file_name", "mode")
#file name can be sample.txt or demo.docx where in mode r: read mode W: write mode
# data = f.read()
# f.close()
# x = create a new file and open it for writing
# a = open for writing, appending to the end of the file if its exists
# b = binary mode
#t = text file
# + open a disk file for upadating (reading and writing)
#with open ("demo.txt", "r") as f:
#       data = f.read()
# print(data)
#deleting files: using the os module
# module (like a code library ) is a file written by another programmer that generally has a function we can use



#create a new file "practice.txt" using pyhton. ADD the following data in it:

#hi everyone \n we are learning file I/O \n using java \n I like programming in java.
with open("practice.txt", "w") as f:
    f.write("hi everyone \n we are learning file I/O \n using java \n I like programming in java.")


#WAF that replace all occurances of "java" with "python " in above file.

with open ("practice.txt", "r") as f:
    data = f.read()
 
new_data= data.replace("java", "python")
print(new_data)

with open ("practice.txt", "w") as f:
    f.write(new_data)

#search if the word "learning" exit or not
word = "xlearning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) !=-1):
        print("found")
    else:
        print("not found")

#waf to find in which line of the file does the word "learning"occur first.
#print-1 if word not found
def check_for_line():
    word = "java"
    data =True
    line_no =1
    with open ("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()





#from a file containing numbers separated by comma, print the xount of even numbers.

# 1, 2 , 45 , 55 , 86 , 76

with open ("practice1.txt", "r") as f:
    data = f.read()
    print(data)
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

#or

count = 0
with open("practice1.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums :
        if(int(val) %2 ==0):
            count += 1
print(count)


