
# Multiplication Table #
    #upto 10#
num = int(input("Enter the number of which you want multiplication table: "))
i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1

    #upto where the user wants#

a = int(input("Enter the number of which you want multiplication table: "))
b = int(input("Enter the number upto where you want multiplication table: "))

i=1
while i <= int(b):
    print(a,"*",i,"=",a*i)
    i=i+1

#asking user to input 10 numbers using one print #

list=[]
for x in range(1,11):
    a= int(input("Enter the value: "))
    list.append(a)
print(list)
print("The sum of given list is: ",sum(list))


#separating a list of even numbers#

for x in range(1,11):
    if x % 2 == 0:
        print(x,"is even number.")
    else:
        print(x,"is odd number.")

# for separating integers strings and float values #

list = ['anything',2,87.098,657,0258.32,'everything']
integer = []
string = []
float_value = []
for x in list:
    if type(x) == int:
        integer.append(x)
    if type(x) == str:
        string.append(x)

    if type(x) == float:
        float_value.append(x)
print(integer)
print(string)
print(float_value)


#for creating and removing numbers from list#
list = []
for x in range(1,11):
    a= int(input("Enter the value: "))
    list.append(a)
print(list)
g = input("Enter the value you want to remove from the list: ")
list.remove(int(g))
print("The new list is: ",list)

# calculator #

a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
c = int(input("Enter your choice of operations:- \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Quit "))

while c!=5:
    if c == 1:
        print("The sum of a and b is: ",a+b)

    if c == 2:
        print("The difference of a and b is: ",a-b)

    if c == 3:
        print("The product of a and b is: ",a*b)

    if c == 4:
        print("The quotient of a and b is: ",a/b)

    if c == 5:
        quit(0)

    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    c = int(input(
        "Enter your choice of operations:- \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Quit "))


    print(quit)

# This much for class 5#