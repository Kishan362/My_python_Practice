#loops in python
print('---------------------for loop------------------')
for item in 'Zero to Mastery':
    print(item)

print('---------------------for loop with list------------------')
for item in [1,2,3,4,5]:
    print(item)

print('---------------------for loop with tuple------------------')
for item in (1,2,3,4,5):
    print(item)

print('---------------------for loop with set------------------')
for item in {1,2,3,4,5}:
    print(item)

print('---------------------for loop with nested loop------------------')

for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item,x)
