def change(some_list):
    some_list[1] = 4

x = [1,2,3]
change(x)
print (x) # Prints out [1,4,3]


def nochange(some_list):
    some_list = 4

x = 1
nochange(x)
print (x) # Prints out 1

# methods are values too
newmethod = change

nochange(x) 
print (x) # Prints out 1



