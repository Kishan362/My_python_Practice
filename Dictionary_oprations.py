#dictionaries in python
#dictionaries are mutable
#dictionaries are unordered
#dictionaries can contain any type of data
#dictionaries are defined by {}
#dictionaries are key value pairs
#dictionaries are like objects in javascript
#dictionaries are like hashmaps in java
#dictionaries are like maps in c++

Dictonary = {
    'name': 'Kishan',
    'age': 20,
    'is_cool': True,
    'fav_color': ['white', 'blue', 'black'],
    123: [1,1,1],
    True : 'Tomato',
    True : 'Potato'
}

#grab key and print values

print(Dictonary['name'])
print(Dictonary['age'])
print(Dictonary['is_cool'])
print(Dictonary['fav_color'])
print(Dictonary[123])
print(Dictonary[True]) # it will print potato because it is the last value of True key

print('----------------------------------------------------')

# methods of dictonary

user = {
    'name': 'Kishan',
    'age': 20,
    'is_cool': True,
    'fav_color': ['white', 'blue', 'black'],
    123: [1,1,1],
    True : 'Tomato'
}

print(user.get('age' ,22))
user2 = dict(name='tota')
print(user2)

print('---------------------Getting key and values -------------------------------')

print('tota' in user2.keys())
print('tota' in user2.values())

print('---------------------clearing and copying -------------------------------')
print(user2.clear())
user2=user.copy()
print(user2)
print(user2.clear())

print('---------------------poping items-------------------------------')

print(user.popitem())
print(user)

print('---------------------updating items-------------------------------')
#updating keyvalues with new item 
print(user.update({'age': 21}))
print(user)