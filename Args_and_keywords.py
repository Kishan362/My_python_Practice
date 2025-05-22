#**args and **keywords in python

#**args is used to pass a variable number of arguments to a function
#**kwargs is used to pass a variable number of keyword arguments to a function

def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

#give me onemore example of **args and **kwargs

def hello(*args, **kwargs):
    print(args)
    print(kwargs)
    print('------------------------')
    print(kwargs['name'])
    print(kwargs['age'])

hello('kishan', 20, name = 'kishan', age = 20)

def function_(name, *args, k='lk', **kwargs):
    print(name)
    print(args)
    print(k)
    print(kwargs)
    print('------------------------')
    total = 0
    for items in kwargs.values():
        total += items
    return name +str (args) + k + str(kwargs) + str(total)
    

print(function_('shraddha', 1,1,1,1, num1 = 1, num2 = 4))
