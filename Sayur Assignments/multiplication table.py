# Printing Multiplication table

num=int(input("enter a number: ")) # num value should contain +ve value
print(f"multiplication table for:{num}")
for i in range (0,10):
    if num>=0: # to whether the given num is +ve or -ve
        i+=1 
        print(num,"x",i,"=",num*i)
else:
    print("Enter a valid number")