#lists in python
#lists are mutable
#lists are ordered
#lists can contain any type of data
#lists can contain duplicates
#lists are defined by []

list1 = [1,2,3,4,5]
list2 = ['a','b','c']
list3 = [1,2,3.33,'a','b','c',True]
print(list1)

print('------------Example List--------------------')
amazon_cart =[
    'notebooks',
    'sunglasses',
    'toys',
    'grapes',
    'pens',
    'jeans',
    'shoes',
    'watches',
    'shirts',
    'pants',
    'socks',
    'hats',
    'fan',
    'toycars',
    'torch',
    'DVDs',
    'Favicol',
    'Chairs'
]
print(amazon_cart)

print('\n-------------Capitalizing each word in list-------------------')
def capitalize_list_items(lst):
    li = []
    for word in lst:
        capitalized_word = word.capitalize()
        li.append(capitalized_word)
    return li
amazon_cart = capitalize_list_items(amazon_cart)
print(amazon_cart)

print('\n--------------Genrating a list using range()------------------\n')
list1to100 = list(range(1,101))
print(list1to100)


print('\n--------------Genrating a sentances using .join()------------------\n')
sentance = '!!!'.join(amazon_cart)
print(sentance)

print('\n--------------List unpacking------------------\n')
a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

#

print('\n--------------Slciing------------------\n')

print('\n\n----------sclicing list---[start 0: end length_of_list: stepover 3]-------------------')
#default value of start is 0 and end is length of list and stepover is 1
#setepover is 3 so it will print every 3rd item
print(len(amazon_cart))
print(amazon_cart[::3])

print('\n\n-------------elements from index 1 up to, but not including, 4----------------')
slice1 = amazon_cart[1:4] # [2, 3, 4] (elements from index 1 up to, but not including, 4)
print(slice1)

print('\n\n-------------printing every second element-------------------')
slice2 = amazon_cart[::2] # [1, 3, 5] (every second element)
print(slice2)

print('\n\n-------------two ways to reverse the list-------------------')
print('using [::-1] method ')
slice3 = amazon_cart[::-1] # [6, 5, 4, 3, 2, 1] (reversed list)
print(slice3)
print("\nusing list.reverse() method ")
slice3.reverse()
print(slice3)

print('\n\n-------------printing item index-------------------')
print(slice3)

print(slice3.index('Pens'))

print('\n\n-------------checking weahter specific item is in list -------------------')

print(slice3)

print('we will get true if item is in list else false we will check for the Torch')
print('Torch' in slice3)



print('\n\n-------------two ways to copy : 1) using .copy() 2) using columns of a list [:]  -------------------')
print('using [:] method ')
amazon_cart[0] = 'Laptop'
nw_cart = amazon_cart[:]
print(nw_cart)

print('\nusing list.copy() method ')
new_cart = amazon_cart.copy()
print(new_cart)
print('\n\n---------------updating list nw_cart-----------------')

nw_cart[0] = 'Gum'
print(nw_cart)

print('\n\n---------------diffrence of nw_cart and amazon_cart-----------------')
print(amazon_cart[0::4])
print(nw_cart[0::4])

print('\n\n-------------appending to list apppended item will be added to last index-------------------')

amazon_cart.append('Phone')
print(amazon_cart)

print('\n\n-------------inserting to list at specific index-------------------')

amazon_cart.insert(0,'Phone')
print(amazon_cart)

print('\n\n-------------extending to list modifys the currant list-------------------')

amazon_cart.extend(['TypeC Cable','Charger'])
print(amazon_cart)

print('\n\n-------------removing from the list - it removes last item from the lise-------------------')

removed_item = amazon_cart.pop() #removes last item

print(amazon_cart)
print(f'\nHere we removed "{removed_item}" from the list')


print('\n\n-------------removing using idex-------------------')
print(amazon_cart)
del amazon_cart[1] 
print(amazon_cart)
print('\nHere we removed "sunglasses" from the list')

print('\n\n-------------removing multiple items using idex-------------------')
print('Before removing\n')
print(amazon_cart)

print('after removing\n')
delted_items = amazon_cart[1:4]
del amazon_cart[1:4] 
print(amazon_cart)

print('\nHere we removed below items from the list')
print(delted_items)

print('\n\n-------------getting the count of values-------------------')
print('here we will get the count of phone form out list')
print(amazon_cart)

countofphone = amazon_cart.count('Phone')
print(f'\nThere are {countofphone} phones in the list')

print('\n\n-------------removing specific item from list-------------------')

print(amazon_cart)
print(amazon_cart.index('Fan'))


amazon_cart.remove('Fan')
print(amazon_cart)
print('\nHere we removed "Fan" from the list')

print('\n\n-------------removing duplicates using set in both lists -------------------')

amazon_cart = list(set(amazon_cart))
print(amazon_cart)
print(f'\n Here we have {len(amazon_cart)} items in amazon_cart')

print('\n\n-------------removing duplicates using set -------------------')

nw_cart = list(set(nw_cart))
print(nw_cart)
print(f'\n Here we have {len(nw_cart)} items in nw_cart')



print('\n\n-------------printing shorted list without modifying the list -------------------')
print(nw_cart)
print('after sorting')
print(sorted(nw_cart))


print('\n\n-------------sorting the list -------------------')
nw_cart.sort()
print(nw_cart)


print('\n\n-------------clearing the list -------------------')
print('Before clearing')
print(nw_cart)
print('After clearing it makes list empty')
nw_cart.clear()
print(nw_cart)
