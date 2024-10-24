#when you know you might get a value that will provide an error, usse try and except
try:
    value = int(input('Enter an integer:'))
    print('The inverse of', value, 'is', 1/value)
except:
    print('You did not provide a number, so I will not calculate the inverse')


try:
    value = int(input('Enter an integer:'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by zero is not posssible, sorry!')


try:
    value = int(input('Enter an integer:'))
    print('The inverse of', value, 'is', 1/value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by zero is not posssible, sorry!')
except:
    print('Something strage happened here, sorry')
