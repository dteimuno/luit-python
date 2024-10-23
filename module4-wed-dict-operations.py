#To create an empthy dictionary and then add items to the dictionary
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

#To update the dictionary:
grades['Anne'] = 'A'
print(grades)

#Another way to update is:
grades.update({'John': 'A'})
print(grades)

#To check key value pairs in a dictionary:
print(len(grades))

#if statement with dictionary:
if 'John' in grades:
    print('John got:', grades['John'])

# To delete a key within a dictionary:
del grades['John']
print(grades)

#Iterate a dictionary
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
for el in grades:
    print(el)
#This shows one part of the dictionary(the keys) and not the values

#This does same as above
for el in grades.keys():
   print(el) 

#for values:
for el in grades.values():
    print(el)

#for both keys and values, you can use the ff:
for person, grade in grades.items():
    print(person, 'got', grade)
#This shows both the keys and values
