for char in 'happy message':
    print(char)

#using if or else to validate if something is in a list
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name?')
if name in invited_guests:
    print('Welcome!')
else:
    print('You are not invited!')

#using not in to check if entity is in a list
invited_guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name?')
if name not in invited_guests:
    print('You are not invited!')
else:
    print('Welcome!')