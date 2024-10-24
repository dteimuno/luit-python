#to type numbers or variables like 1-100 in a long list,
#This is a longer way to do it
numbers = []
for i in range(1,101):
    numbers.append(i)
print(numbers)
#here we inserted the numbers 1-100 into i as a list

#a shorted way of getting numbers into a list
numbers = [i for i in range(1,101)]
#here we said i for i in range, not just for i in range. If we don't do this we will get an error
print(numbers)

#trying out another way with list comprehension 
numbers = [i for i in range(1,101) if i % 3 != 0]
print(numbers)