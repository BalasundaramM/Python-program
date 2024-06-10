'''write the python dictionary program to get input (fruits) from the user .
and display the output how fruits in the dictionary in keys and values'''

fruits_lists={}
while True:
    fruit = input("Enter a fruit (or 'done' to finish): ").strip().lower()
    if fruit == 'done':
        break
    if fruit in fruits_lists:
        fruits_lists[fruit] += 1
    else:
        fruits_lists[fruit] = 1


print("\nFruits in the dictionary:")
for fruit, count in fruits_lists.items():
    print(f"{fruit}: {count}")
