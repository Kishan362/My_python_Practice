#you can make strings with ' and "" .

print(type('hi stranger'))

username = 'superscientist'
password = 'supertopsecret'

long_string = '''
WOW
O O
---
'''
# three ''' is used for multi line string

print(long_string)

print('--------------------------------')

first_name = 'Kishan'
last_name = 'Lal'
full_name = first_name + ' ' + last_name
print(full_name)

#string concatenation
print('hello' + ' Kishan')

#string concatenation only works with strings
# print('hello' + 5) # this will throw an error
print('--------------------------------')
# type conversion
print(type(str(100)))
print(type(int(str(100))))

a = str(10000)
b = int(a)
c = type(b)
print(c)

print('hello' + str(5)) # this will work

print('--------------------------------')
#escape sequence

#\t is used for tab
#\n is used for new line
weather = "\tIt's a \"kind of\" sunny day \n\t hope you have a Great Day!"
print(weather)


print('--------------------------------')

#formatted strings
name = 'kishan'
age = 20
print(f'hi {name}. You are {age} years old')

# string indexes 

#here [start] : [stop] : [stepover]


selfish = 'Oh my god'
        #  012345678
print(selfish[0])
print(selfish[1])
print(selfish[2])
print(selfish[7]) 
print(selfish[0:5]) # this will print OH My
print(selfish[0:8:3]) #this will print omg start at 0 end at 8 and stepover 3  
print(selfish[1:]) # this will print e me me
print(selfish[:5]) # this will print Oh m
print(selfish[::1]) # this will print Oh my god
print(selfish[-1]) # this will print d
print(selfish[-3]) # this will print y
print(selfish[::-1]) # this will print dog ym hO


print('--------------------------------')
# immutability

# strings do not change you have to change it whole 

selsel= '01234567'
selsel= selsel + '8'
print(selsel)