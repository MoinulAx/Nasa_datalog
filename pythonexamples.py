# 1.1 Evaluate expressions to identify the data types Python assigns to variables

x = True

print(type(x)) # bool



# 1.2 Perform and analyze data and data type operations

x = 2

y = "4"

print (x + int(y))



# 1.3 Determine the sequence of execution based on operator precedence

print(3 + 4 * 2)



# 2.1 Construct and analyze code segments that use branching statements

a=input("do u suck ")

if a =="yes":
    print("correct")
else:
    print("are u sure bout that ")

#---------------------------------------------------#

#Example 2 

b=input("are u a boy or girl ")

if b=="boy":
    print("BOY")
elif b=="girl":
    print("GIRL")
else:
    print("protractor")
    if b=="neither":
        print('noice')

# 2.2 Construct and analyze code segments that perform iteration


c=[1,2,3,4,5,6,7,8,9]
 
for i in c:
    if i==9:
        print("Nineeeeeeeee")
        break 
    else:
        print(i)

#---------------------------------------------------#

#Example 2

d=0
while True:
    if d<=10:
        print(d)
        d+=1
    else:
        print("numbers")
        break

#Construct and analyze code segments that perform console input and output operations
#• Read input from console, print formatted text (string.format() method, f-String method), use command-line arguments

e=input("food name")

print(f"meat and {e}")

#---------------------------------------------------#

#Example 2

f=input("person name ")

g=input("person age ")

print("your name is {} and you are {} years old".format(f,g))

