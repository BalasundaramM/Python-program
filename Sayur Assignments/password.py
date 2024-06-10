# Validation Program for Password checking
import sys

password=input("Create Password with minimum 8 characters: ")

alpha_count=0 #create a variable store the count of variables
num_count=0
special=0
if len(password)>=8: #it checks the length of the password whether is greater or equal to 8
    
    for i in password: # it splits the password string into characters
        
        if i.isalpha(): # if the given password has the alphabet characters then the count will increase
            alpha_count += 1

        elif i.isnumeric(): #if the given password has the number then the count will increase
            num_count += 1 
        
        else: #if the given password has the special characters then the count will increase
            special += 1
           
    
    if( password.isalpha() ==True) or (password.isnumeric() ==True) or (special >=8):
        print("Your password is weak.")
        
        '''if the given (number or alphabet or special character) in this any one value was written 
        and it is greater or equal to 8 then it print the password is weak'''
        
        sys.exit()
        
    elif( alpha_count >=3 and num_count >=2 and special >=1):
        
        '''if the given password has alphabet greater or equal to 3 
        and number count is greaterthan or equal to 2 
        and special character is greater than or equal to 1 '''
        
        if len(password) >= 16: 
            
            '''if the above elif condition has satisfied then it will check whether 
            if the password is greater than or equal 16 then it prints the password is very strong
            else it is strong'''
            
            print("Your password is Very strong")
        else:    
            print("Your password is strong")
            sys.exit()

    else:
        '''in this if the given password is (alphabet , number and special characters)
          the three variables are greater than or equal to 1 then it prints the password is ok'''
        
        print("Your password is Ok")                

    
#if password length is less than 8 then it prints password is too short
else:
    print("your password is too short")