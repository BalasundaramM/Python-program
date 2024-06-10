'''
Write a program to continuously get firstname and last name 
of various students from the user.Stop when the user's first name 
or last name starts with "Z".
'''

name=True
Name_count =0

while (name ==True):
    Name_count +=1
    First_name=input(f"Enter your First_name {Name_count}: ")
    First_name_length = len(First_name)
    if First_name.startswith('z') or First_name.startswith('Z'):
        name==False
        print("First Name should not startswith z or Z")
        break
    elif (First_name.isalpha()==False):
        print("last Name should not contain any numbers")
           
    elif First_name_length < 3:
        print("Invalid name") 
        


    Last_name=input(f"Enter your Last_name {Name_count}: ")
    Last_name_length = len(Last_name)
    if Last_name.startswith('z') or First_name.startswith('Z'):
        name=False
        print("Last Name should not startswith z or Z")
        break
    elif (Last_name.isalpha()==False):
        print("Last Name should not contain any numbers")  
        print("the Name will not print Because First name or Last name has contain numbers ")
        
    elif Last_name_length < 3:
        print("Invalid name")
    
      
    First_name=First_name.capitalize()
    Last_name=Last_name.capitalize()
    if(First_name.isalpha()==True or Last_name.isalpha()==True):
        print(f"Name {Name_count}:",First_name +' '+ Last_name)        