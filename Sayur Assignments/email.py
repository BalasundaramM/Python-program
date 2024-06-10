# Validating a Email address

import sys
email=input("enter your email_id: ")

if len(email) < 10:
     print("Email_id short ")
     sys.exit()

if email.count('@')>1:
    print('invalid email_id contains more @. no of occurrence: ',email.count('@'))
    sys.exit()

elif email.count('.')>=1 and email.count('@')==0:
    print('invalid @ character is not included')
    sys.exit()

elif email.count('@')==1 and email.count('.')==0:
    print('invalid . character is not available')
    sys.exit()

split_email=email.split('@')
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

