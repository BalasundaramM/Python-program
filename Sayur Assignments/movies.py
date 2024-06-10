#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the movie"
#Continue until they is atleast 3 movies they both like

friend1=input("What movies would you like?: ")
friend1=friend1.split(',')

friend1_2_moviecount=0
friend1_2_movieliked=[]
while(True):
    friend2=input("What movies would you like?: ")
    if (friend2 in friend1) and (friend2 not in friend1_2_movieliked):
        friend1_2_moviecount +=1 
        friend1_2_movieliked.append(friend2)
        print("You both like: ",friend2) 
        if friend1_2_moviecount >=3:   
            break
    else:
        print("Try again")
           

print("The Movies you both liked is: ",friend1_2_moviecount)   
print("The movies you were liked: ",friend1_2_movieliked)     