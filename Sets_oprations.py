#sets in python
#sets are mutable
#sets are unordered
#sets can contain any type of data
#sets are defined by {}
#sets are like dictionaries but they are unordered
#sets are like lists but they are unordered
#sets are like tuples but they are unordered
#sets are used for data that will not change
#sets are used for data that will not have duplicates


print('---------------------set only takes unique values----------------')
my_set = {1,2,3,4,5,5,4,3,2,1} # it will only take unique values
print(my_set)

print('---------------------adding and removing items from set----------------')
my_set.add(6)
print(my_set)
my_set.remove(6)
print(my_set)

print('---------------------clearing set----------------')
my_set.clear()
print(my_set)

print('---------------------copying set----------------')
my_set = {1,2,3,4,5}
new_set = my_set.copy()
print(new_set)

print('---------------------clearing new_set----------------')
my_set.clear()
print(my_set)

print('---------------------removing dublicates from list using set----------------')
my_list = [1,2,3,4,5,5,4,3,2,1]
new_list = list(set(my_list))
print(new_list)

print('---------------------set does not support indexing----------------')
my_set = {1,2,3,4,5}
# print(my_set[0]) # it will give error

print('---------------------only way to check is by using itrator----------------')
print(3 in my_set)

print('---------------------cheking lenth of set----------------')
print(len(my_set))

print('---------------------set methods------------------')
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print('---------------------difference------------------')
print(my_set.difference(your_set)) # it will print {1, 2, 3} because it is not in your_set
print('---------------------discard------------------')
# my_set.discard(5) # it will remove 5 from my_set
# print(my_set)
print('---------------------intersection------------------')
print(my_set.intersection(your_set))
print('---------------------anotherway to do intersection------------------')
print(my_set & your_set)
print('---------------------isdisjoint------------------')
print(my_set.isdisjoint(your_set))
print('---------------------issubset------------------')
print(my_set.issubset(your_set))
print('---------------------issuperset------------------')
print(my_set.issuperset(your_set))
print('---------------------union------------------')
print(my_set.union(your_set))
print('---------------------anotherway to do union------------------')
print(my_set | your_set)
print('---------------------update------------------')
my_set.update(your_set)
print(my_set)
print('---------------------difference_update------------------')
my_set.difference_update(your_set)
print(my_set)