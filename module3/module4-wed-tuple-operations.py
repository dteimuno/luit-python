#show number of entities in a tuple
user_data = ('John', 'American', 1964)
print(len(user_data))

user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This person comes from the US')

#iterate tuple with for loop
user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)

#plus operator with tuple
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

#multiplication operator with tuple
numbers = (0, 1) * 10
print(numbers)

user_data = ('John', 'American', 1964)
