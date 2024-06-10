# Printing Menu for Hotel

menu = {
    "Starters": {"Greek Salad": 100, "Chicken wings": 70, "Bread chicken wings": 60, "Chicken Pakoda": 70},
    "Main_course": {"(Ts,s)Chicken Biriyani": 120, "Fish Biryani": 170, "(Ts)Mutton Biriyani": 300, "Leaf Biriyani": 150},
    "Desserts": {"Choco lava cake": 130, "Jigartanda": 140, "Choco Brownie": 120, "Oreo Shake": 180}
}

print("Welcome to Hungry Eatery")
print("If you want Menu Choose '1'")
print("If you want to add a Food Item choose '2'")

def print_menu():
    print("Here is our Menu:")
    print("Ts - too spice  , s - spice")
    for category, foods in menu.items():
        print(f"\n{category}\n")
        for item, price in foods.items():
            print(f"\t{item} \t-\t {price} Rs")

def add_item():
    category = int(input("In which category do you want to add the item?\nEnter 1 for Starters, 2 for Main_course, 3 for Desserts: "))
    if category == 1:
        category_name = "Starters"
    elif category == 2:
        category_name = "Main_course"
    elif category == 3:
        category_name = "Desserts"
    else:
        print("Invalid category! Returning to main menu.")
        return

    name = input("Enter the food item name: ")
    price = int(input("Enter the price: "))
    menu[category_name][name] = price
    print(f"{name} has been added to {category_name}.")

def add_more_items():
    while True:
        add_more = input("Do you want to add more items? (y/n): ")
        if add_more.lower() == "y":
            add_item()
        elif add_more.lower() == "n":
            print_menu()
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

choice = int(input("Enter your choice: "))
if choice == 1:
    print_menu()
elif choice == 2:
    add_item()
    add_more_items()
else:
    print("Invalid choice!")
