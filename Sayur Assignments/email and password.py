#Validating Email Address and password

import sys
#For username

# first we want to get the user name
username = input("Enter the Username: ")

# in this we want to assign the endswith characters
username_char=('.com','.edu','.tech','org')

#check whether the username contain @ charcter or not it @ not present it will print to insert @ character
if '@' not in username :
    print("username must contain the special character @ ")
    sys.exit()

# check whether the username has dot function or not
elif '.' not in username:
    print("user name must contain dot") 
    sys.exit()   

# in this the username should contain only one @     
elif username.count('@') >1:
    print("username must contain only one @ ")
    sys.exit()

# after checking the username then whether the username is endswith anyone of the given userneme_char
elif (username.endswith(username_char)==False):
    print("Username must endswith the anyone of the given username_char ")
    sys.exit()

#For password
    
#split the username into first domain and last domain name
split_username=username.split("@")
first_domain=split_username[0]
last_domain=split_username[1]

#check the last domain name startswith companyname before dot and after @
if last_domain.startswith("."):
    print("give your company name before dot and after @")
    sys.exit()

# split the last portion from  the last domain by using dot into company name and lastword
split_last_portion=last_domain.split(".")
company_name=split_last_portion[0]
last_word=split_last_portion[1]

#create variable for first , second , third , fourth character
first_char=first_domain[0]
second_char=first_domain[2::]
third_char=company_name[0:3:1]
fourth_char=input("Enter your DOBY: ") #for fourth character ask the user birth year


password=first_char + second_char + third_char + fourth_char
print("Username: ",username)
print("Password: ",password)