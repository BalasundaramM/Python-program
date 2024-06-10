# Validating a Member age

import sys
Member=int(input("How many Member in your family: "))
minor_count=0
major_count=0
Senior_citizen=0

if Member < 1:
    print("The Family should contain Atleast 1 member")
    sys.exit()

for i in range(Member):
    Age=int(input(f"Enter the age of Member {i+1} : "))
    if Age >=110:
        print("Age should not exceed 110")  
        sys.exit()
    if Age <=0:
        print("the given Age is below 0")   
        sys.exit()

    if Age <18 :
        minor_count+=1
        print("your are Minor")
    elif Age >= 18 and Age <=59 :
        major_count +=1
        print("you are major")
    elif Age >=60:
        major_count +=1
        Senior_citizen +=1 
        print("you are Senior citizen")
    

print("Number of Minor count: ",minor_count)
print("Number of Major count: ",major_count)
print("Number of Senior Citizen count: ",Senior_citizen)         



               

    