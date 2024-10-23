#swapping variables
first = input('enter your first number:')
second = input('enter your second number:')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)

#second method
first = input('enter your first number:')
second = input('enter your second number:')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

#This can also be done with lists
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

#to sort alphabetically
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

#to sort from lowest to highest number,
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

#to sort from highest value to lowest value,
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

#to show sorted and then just regular list,
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)

#remember, for e.g. list_name.sort(): sorts the original list and is unchangeable after; and sorted(list_name): gives back a new, sorted list, keeps the original unchanged
