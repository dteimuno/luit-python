top_cities = ['New  York  City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[2]
print(top_cities)

print(top_cities[2])

top_cities = ['New  York  City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[3:]
print(top_cities)

top_cities = ['New  York  City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[:]
print(top_cities)

#del is not a function call. It's an instruction
top_cities = ['New  York  City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities
print(top_cities)
#This shoul produce an error since once you delete the entire function there is nothing to print!


