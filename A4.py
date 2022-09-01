it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#To find the length of it_companies
print(len(it_companies))

#To add Twitter to it_companies
it_companies.add('Twitter')
print(it_companies)

#Inserting multiple IT companies to set it_companies
list=('TCS','SVK','Zelecloud')
it_companies.update(list)
print(it_companies)

#To remove one of the company from the set
it_companies.remove('Zelecloud')
print(it_companies)

#Difference between remove and discard : Both remove() and discard() are used for deleting the elements from the set but if the element is not present in the set, remove method raises a key error exception where discard method do not raise an error.

#To join A and B
print(A|B)

#To find A intersction B
print(A&B)

#To find Is A subset of B
print(A .issubset(B))

#To find out whether A and B disjoint set
print(A .isdisjoint(B))

# Join A with B and B with A
A.update(B)
print(A)
B.update(A)
print(B)

#To find the symmetric difference between A and B
print(A^B)

#To delete the sets completely
del A
del B
del it_companies

#Converting the ages to a set
lengthlist=len(age)
set_ages=set(age)
lengthset=len(set_ages)

#comparing the length of the list and the set.
if(lengthlist==lengthset) :
 print("length of the list is equal to length of the set")
else :
 print("length of the list is not equal to length of the set")
if(lengthlist<lengthset) :
    print("length of the list is less than length of the set")
else :
    print("length of the list is not less than length of the set")
if(lengthlist>lengthset):
  print("length of the list is greater than length of the set")
else:
  print("length of the list is not greater than length of the set")