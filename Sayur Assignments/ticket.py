#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.

ask_count=0
money_got=0

for i in range(5):

    Money=int(input(f"{i+1}. Give me some Money for to get ticket for cinema: "))
    ask_count+=1
    money_got +=Money
    if ask_count >=5 and money_got <1000:
        print(f"Thank you ,I got only {money_got} and the count has been over.")
        break
    if Money >10:
        if money_got <1000:
            print("Thank you!,But I need some more money")
        elif money_got ==1000:
            break
        elif money_got > 1000:
            print("Thank you for giving some extra money")
            break

    else:
        print("please give me a some more money")

print(f"\nThank you! I got :{money_got} Rs for the Movie ticket")
print(f"For collecting this money I asked {ask_count} times from My Parents")