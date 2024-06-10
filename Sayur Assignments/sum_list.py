'''Add two number represented in a list as reversed. print the sum also as a list in reverse order
eg input list1 = [1,2,3] list2 = [5,6,7]
answer= [6,8,0,1]
explanation (321 + 765 = 1086)'''

list1 = [1, 2, 3]
list2 = [5, 6, 7]
total_list = []

for a, b in zip(list1, list2):
    total = a + b
    digits = list(str(total))
    for digit in reversed(digits):
        total_list.append(int(digit))

print (total_list)
