print('Hello', 'How are you?', end='.', sep='-')

def print_letter_count(text='This is the default string to search', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

#Unlike the previous part in the module(function-params), since letter=a, we don't have to add that part again when we invoke our functionm
print_letter_count('How many letters a are here?')

#Since both variables are made known in the function we don't have to insert the variables anytime we call the function:
print_letter_count()