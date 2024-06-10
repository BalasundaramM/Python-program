#Write a program to get first name, last name, age, phone number and email id 
#from the user. Validate all the inputs and print the user information in a 
# readable manner.User's name must be printed in capital letters (or first letter should be capital). 
# Phone number must contain 10 digits and no alphabets. 
# Email id must contain a dot and @. 
# Age must be a valid number.

import sys

#for Name
First_name=input("Enter your First_name: ")
First_name_length = len(First_name.strip())
if First_name_length < 3:
	print("Invalid name")
elif (First_name == First_name.lower()) or (First_name[0] == First_name.lower()):
    print("Invalid First_name not contains upper case.")
    sys.exit()

Last_name=input("Enter your Last_name: ")
Last_name_length = len(Last_name.strip())
if Last_name_length < 3:
	print("Invalid name")
elif (Last_name == Last_name.lower()) or (Last_name[0] == Last_name.lower()):
    print("Invalid Last_name not contain upper case.")
    sys.exit()

#for Age
Age=input("Enter your Age: ")
if(Age.isdigit()==False):
    print("invalid,Check the given Age.")
    sys.exit()
Age=int(Age)
if Age<=0 or Age>=100:
     print("Invalid Age.")   
     sys.exit()      

#for Phone number
Phone_number=input("Enter your phone number: ")
Phone_number_length=len(Phone_number.strip())
if Phone_number.isalpha()==True:
    print("Invalid,it contains Alphabets.") 
    sys.exit()
Phone_number_length=int(Phone_number_length)
if(Phone_number_length < 10) or (Phone_number_length > 10) : 
    print("Invalid, please enter the 10 digit number")
    sys.exit()
Phone_number_length=int(Phone_number)    
if Phone_number.startswith('0'):
     print("number should not start with 0")   
     sys.exit() 

# for Email
Email_id=input("Enter your Email_id: ")
if len(Email_id) < 10:
     print("Email_id short ")
     sys.exit()

if '@' not in Email_id or '.' not in Email_id:
    print("Invalid, Email_Id not contains @ and dot.")

if Email_id.count('@')>1:
    print('invalid email_id contains more @. no of occurrence: ',Email_id.count('@'))
    sys.exit()

elif Email_id.count('.')>=1 and Email_id.count('@')==0:
    print('invalid @ character is not included')
    sys.exit()

elif Email_id.count('@')==1 and Email_id.count('.')==0:
    print('invalid . character is not available')
    sys.exit()

split_email=Email_id.split('@')
first_portion=split_email[0]
last_portion=split_email[1]

if first_portion.isalnum()==False:
    print("user cannot contain special character")
    sys.exit()

last_portion_split= last_portion.split(".")
domain=last_portion_split[0]
end=last_portion_split[1]
if len(domain) <= 3:
    print("domain name must be min 3 character")
    sys.exit()   

print()
print("Firstname: ",First_name) 
print("Lastname: ",Last_name)    
print(f"Your Name is: {First_name} {Last_name}")     
print("Age: ",Age)
print("Phone number: ",Phone_number) 
print("Email id: ",Email_id)