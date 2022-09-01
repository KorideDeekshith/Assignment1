#Creating two tuples
brothers= ("sai","sumith")
sisters=("reshma", "sri")

#Joining two tuples
siblings=brothers+sisters
print(siblings)

#To display the number of siblings
print(len(siblings))

#Modifying the tuple to list
y=list(siblings)

#adding mother and father to the list
y.append("laxmi")
y.append("anand")

#converting list back to tuple
family_members=tuple(y)
print(family_members)