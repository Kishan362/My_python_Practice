#enumerate in python
print('---------------------enumerate------------------')
for i, char in enumerate('Hellooo'):
    print(i, char)

print('---------------------enumerate------------------')
for i, char in enumerate([1,2,3,4,5]):
    print(i, char)

print('---------------------enumerate------------------')
for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 49:
        print(f'index of 49 is: {i}')



