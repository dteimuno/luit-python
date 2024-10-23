empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1,2,3,
print(three_el_tuple)

#tuples prefer round bracktes while lists prefer square brackets
#you can't append to a tupple once you define a tuple
user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980)

#The following below are for learning. They will provide errors and prevent you from moving along
user_data.append('teacher')#this should produce an error

del user_data[0] #this should produce an error because user_data is a tuple not a string

print(user_data[0])
user_data[0] = 'Mark'# This should produce an error. Tuples won't allow you to change what is within

#strings are also immutable. Trying to change a string should produce errors
message = 'welcome'
message = 'Welcome'
message[0] = 'w'
#You should get an error

