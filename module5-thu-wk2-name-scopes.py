def show_truth():
    mysterious_var = 'Surprise!'
    print(mysterious_var)

show_truth()

#Using global and local variables we get get different values whown to us:
def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)
#This is what is called shadowing. We insert global into our function to make sure anything after our function is called is represented by the global variable

#With lists,
def show_truth():
    mysterious_var.append = ('New Surprise!')
    print(mysterious_var)

mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth()
print(mysterious_var)
