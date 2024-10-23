numbers = [1, 2, 3, 4]
countries = ['UK', 'US', 'Germany']

#not recommended but python allows you to make two different data types
countries = [1, 'UK', 2, 'US']

#this is a nested list
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])
#to access index within a sublist, e.g. index 0 from 0, use the following:
print(cells[0][0])
print(cells[0][1])
print(cells[1][2])

#using for loop within nested list
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element', x)

#for nested within nested list:
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)

#as if in data manipulation:
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)

table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#inner list comprehension
table = [[i for i in range(1,6)] for j in range(4)]
#this means repeat i(the first part) four times(the second part of the list)
print(table)



