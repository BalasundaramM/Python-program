# Check the maximum number and minimum number

num1=int(input("enter the 1st number:"))
num2=int(input("enter the 2nd number:"))
num3=int(input("enter the 3rd number:"))
print(num1)
print(num2)
print(num3)
if num1>num2 & num1>num3 or num1<num2 & num1<num3 :
  print("num1 is greater.")
  print("num1 is smaller")
elif num2 > num3 & num2<num3:
  print("num 2 is greater.")
  print("num2 is smaller.")  
else:
  print("num3 is greater.")
  print("num3 is smaller")