# Checking whether the given number is Armstrong or not

num=int(input("Enter a number: "))
a=0
num_length=num

while (num_length>0):
    num1=num_length%10
    a+=(num1**3)
    num_length=num_length//10
if(a==num):
    print("it is Armstrong number")
else:
    print("it is not Armstrong a number")    

