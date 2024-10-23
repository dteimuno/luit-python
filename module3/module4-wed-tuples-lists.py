city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.5)

#tuples in list
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.5) ]
for capital in capitals:
    print('Name:', capital[0], ',Country:', capital[1], ',Population:', capital[2])

#list in tuples:
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
print(user_data[3])

#to append to the list within a tuple; list is mutable and can be changed, tuple can't
user_data[3].append(79.6)
print(user_data)