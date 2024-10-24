fav_band = 'Green Day'
print(fav_band[6])

print(fav_band[:6])

#capitalization string method
text = 'please capitallize me'
text_cap = text.upper()
print(text_cap)

#using the .numeric string method to check if an input is a number or not
user_number = input('Please provide a number:')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')
    