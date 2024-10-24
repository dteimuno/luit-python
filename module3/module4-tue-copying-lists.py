#The ff updates the name_new variable but then when name_original is used it shows a new variable
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)

#however, this workss differently for lists as shown below:
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)
#the result this time unlike the first example shows that with lists once you modify a lisst that is tied together, other lists will be modified too

#to modify an equated list but not modify both lists, use slicing
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
#this replaces index 0 in list_original with 5
print('Original:', list_original, '\nNew:', list_new)

#to modify a list,
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
#this modifies the value of list_original
print('Original:', list_original, '\nNew:', list_new)