print('hello')
name = input('name?')

#append is a method not a function! Methods are functions that belong to specific data
book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4)
print(book_ratings)

book_ratings = [7, 9, 5, 6, 8]
book_ratings.insert(1, 10)
#above inserts the value of 10 at index #1
print(book_ratings)