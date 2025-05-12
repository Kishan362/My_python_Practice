#tuples in python
#tuples are immutable
#tuples are ordered
#tuples can contain any type of data
#tuples are defined by ()
#tuples are like lists but they are immutable
#tuples are faster than lists
#tuples are used for data that will not change

my_tuple = (1,2,3,4,5)
print(my_tuple)

print('---------------------indexing-------------------')
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[4])

print('---------------------slicing-------------------')
print(my_tuple[0:3])
print(my_tuple[1:4])
print(my_tuple[2:5])

print('---------------------cheaking if item is in tuple-------------------')
print(5 in my_tuple)
print(6 in my_tuple)

print('---------------------using tuple in dictonary-------------------')
user = {
    (1,2): 'hello',
    (3,4): 'hi'
}
print(user[(1,2)])
print(user[(3,4)])

print('---------------------using tuple methods-------------------')
my_tuple = (1,2,3,4,5,6,7,8,9,10)
new_tuple = my_tuple[1:6]
print(new_tuple)

print('---------------------assiging tuple to variables-------------------')

my_tuple = (1,2,3,4,5,6,7,8,9,10,10)
# print(x)
# print(other)

print('---------------------counting items in tuple-------------------')
print(my_tuple.count(5))
print(my_tuple.count(10))

print('---------------------finding index of item in tuple-------------------')
print(my_tuple.index(5))
print(my_tuple.index(10))
