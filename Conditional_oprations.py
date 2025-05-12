#conditional oprations in python
is_old = True
is_licenced = True

password= '123'
username = 'admin'


if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')
else:
    print('you are not of age!')


#turnary oprator
is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed to message'
print(f'user {username} is {can_message}')

is_user = False  

#short circuiting
if is_friend or is_user:
    print('you can message')
else:
    print('you can not')




print('----------------------------------------------------------------')
#truthy and Falsey
print(bool('hello')) # this will print true
print(bool(5)) # this will print true
print(bool(0)) # this will print false
print(bool('')) # this will print false
print(bool(None)) # this will print false
print(bool([])) # this will print false
print(bool({})) # this will print false
print(bool(())) # this will print false
print(bool(False)) # this will print false
