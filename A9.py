#creating an empty set for input
w_lbs = []
list = int(input("Enter the no. of students"))
print("Enter the weights of students")

#Function to convert lbs to kgs
for i in range(list):
    w = float(input())
    w_lbs.append(w)
print(w_lbs)

#creating an empty list for output in kgs
w_kgs= []

#calling function with required input
for a in w_lbs:
    w_kgs.append(round(a / 2.20462262, ndigits = 2))
print(w_kgs)