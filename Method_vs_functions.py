#method vs functions in python

#method is a function that is defined inside a class
#function is a function that is defined outside a class

#method
list1 = [1,2,3,4,5]
list1.append(6)
list1.pop()
print(list1)
a = 'this is a string'
b = a.upper()
b = a.endswith('s')
print(b)



#function
def say_hello():
    '''
    this function says hello
    '''
    print('hello')



a = say_hello()
print(a)


