# Validating phone number

import sys
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

print(f"Your phone number {Phone_number} is valid")     