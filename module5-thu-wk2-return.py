def get_average(input_numbers):
#This is a function we have generate to define the average value with respect to input numbers
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average

print('The average is:', get_average([5.0, 3.5, 9.9, 10.0]))

def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
    print('Show me!')
print(get_average([2]))

def is_first_last_equal(number_list):
    if(number_list[0] == number_list(-1)):
        return True
    else:
        return False

print(is_first_last_equal([10, 20, 30, 40, 10]))

