# Eliminating  the repeating numbers
# example=[1,2,3,4,4,4,5,5,5,5,6,6,1,1,2,2,3,3]
# output=[1,2,3,4,5,6] 

list=[1,2,3,4,5,5,5,4,4,3,3,1,1]
final=[]
count=0
for i in list:
    if not i in final:
        final.append(i)
    else:
        count+=1
print(final)        
