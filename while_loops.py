#while loops in python
print('---------------------while loop------------------')
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print('done!')

print('---------------------while loop with break------------------')
i = 0
while i < 50:
    print(i)
    i += 1

else:
    print('done!')


print('---------------------while loop with list------------------')
my_list = [1,2,3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

print('---------------------while True loop------------------')
while True:
    response = input('say something: ')
    if (response == 'bye'):
        break
