# Checking whether the given number is ODD or EVEN.

num=int(input("Enter a number: "))
sum_odd=0
num1=0
sum_even=0

while (num>0):  
    num1=num%10

    num=num//10
    n=num1
    if(n%2!=0):
        sum_odd+=n
        
    else:
        sum_even+=n
print("The sum of even numbers are: ",sum_even)  
print("The sum of odd numbers are: ",sum_odd)