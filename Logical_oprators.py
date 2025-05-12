#logical oprators in python
print('---------------------logical oprators------------------')
print('---------------------and------------------')
print(1 < 2 < 3) # this will print true
print(1 < 2 > 3) # this will print false
print(1 < 2 and 2 < 3) # this will print true
print(1 < 2 and 2 > 3) # this will print false
print('---------------------or------------------')
print(1 < 2 or 2 < 3) # this will print true
print(1 < 2 or 2 > 3) # this will print true
print(1 > 2 or 2 > 3) # this will print false
print('---------------------not------------------')
print(not 1 < 2) # this will print false
print(not 1 > 2) # this will print true

print ('---------------------is------------------')
print(1 is 1) # this will print true
print(1 is 2) # this will print false
print(1 is not 2) # this will print true
print(1 is not 1) # this will print false

print ('---------------------in------------------') 
print(1 in [1,2,3]) # this will print true
print(1 in [2,3,4]) # this will print false
print(1 not in [1,2,3]) # this will print false
print(1 not in [2,3,4]) # this will print true




print ('---------------------Logical oprators excercise------------------')

#logical oprators excercise
is_magician = True
is_expert = False

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('at least you are getting there')
elif not is_magician:
    print('you need magic powers')


print('-----------------is vs == ecercise---------------')
print(True == 1) # this will print true
print('1' == 1) # this will print false
print([] == 1) # this will print false
print(10 == 10.0) # this will print true
print([111,112,113] == [111,112,113]) # this will print true

print('-----------------is vs == ecercise---------------')
print(True is 1) # this will print false
print('1' is 1) # this will print false
print([] is 1) # this will print false
print(10 is 10.0) # this will print false
print(10 is 10)

a = [1,2,3]
b = [1,2,3]
print(a == b) # this will print true]
