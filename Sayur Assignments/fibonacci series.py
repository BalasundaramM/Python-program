#fibonacci series


a=int(input("Enter the first number: ")) #get the first number
b=int(input("Enter the second number: ")) # get the second number
l=int(input("enter the loop number: ")) # to set a loop limit
c=0 # temp variable to store the third value

for i in range(0,l):
    
    c=a+b
    a=b
    b=c
    print(c)