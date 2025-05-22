#walrus oprator in python
a ='kem 6 kem 6 maja ma ne ?'

if ((n := len(a)) > 10) :
    print(f'too long {n} elements')

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)

#one more example of walrus oprator