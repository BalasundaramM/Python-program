#Printing 
#For A
num_rows=int(input("Enter no of Rows: "))
num_cols=int(input("Enter no of columns: "))
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if row==(num_rows//num_rows) or col==num_cols or col==num_cols//num_cols or row==(num_rows//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')
print(' ')

#For B

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if col==1 or (row==1 and col<=3) or (row ==2 and col==num_cols) or (row ==3 and col== num_cols) or (row==4 and col<=3) or (row ==5 and col==num_cols) or (row ==6 and col==num_cols) or (row==num_rows and col<=3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')   
print(' ')

# For C

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if (2<=row<=4 and col==1) or (row==1 and col>=2) or  (row==5 and col>=2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')  
print(' ')    

#for D

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if col==1 or (row==1 and col<=3) or (2<=row<=4 and col==4) or (row==5 and col<=3):
            print('*',end=' ')
        else:
            print(' ',end=' ')  
    print('')      
print(' ')

#For E

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if col==1 or row==1 or row==3 or row==num_rows*1:
            print('*',end=' ')
        else:
            print(' ',end=' ')  
    print('')                                           
print(' ')

#For F

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if col==1 or row==1 or row==3 :
            print('*',end=' ')
        else:
            print(' ',end=' ')  
    print('')   
print(' ')                                                    

#For G

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if col==1 or (row==1 and col<=4) or (row==5 and col<=4) or (col==4 and 3<=row<=5) or (col==5 and 3<=row<=5):
            print('*',end=' ')
        else:
            print(' ',end=' ')  
    print('')   
print(' ')   

#For H

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if col==1 or col==num_cols or row==3:
            print('*',end=' ')
        else:
            print(' ',end=' ')  
    print('')   
print(' ')   

# FOR I

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if row==1 or row== num_rows or col==3:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')
print(' ')

# FOR J

num_rows=int(input("Enter no of Rows: ")) 
num_cols=int(input("Enter no of columns: ")) 
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if row==1 or (row==5 and 1<=col<=2) or (col==1 and 4<=row<=5) or col==3:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')
print(' ')

#For L
num_rows=int(input("Enter no of Rows: "))
num_cols=int(input("Enter no of columns: "))
for row in range(1,num_rows+1):
    for col in range(1,num_cols+1):
        if col==1 or row==num_rows:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('')
print(' ')
