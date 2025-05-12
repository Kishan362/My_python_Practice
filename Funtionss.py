# functions in python
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


def fun_xyx():
    print('hello functionss')

fun_xyx()


def fun(fill1 , fill2):
    for row in picture:
        for pixel in row:
            if (pixel == 1):
                print(fill1, end='')
            else:
                print(fill2, end='')
        print('')


fun('o',' ')
fun('x',' ')
fun('y',' ')


def fun_Hola(name='anonymous', age = 55, emoji= ':)') :
    print(f'hi {name} you are {age} years old {emoji}')

fun_Hola('topa',22, '(~ _ o)')

#positional arguments
#keyword arguments
fun_Hola(age= 22, emoji='(~ _ o)', name ='Gota')
#default parameters
fun_Hola('kk')

#return statement
def sum(num1, num2):
    return num1 + num2
total = sum(4,5)
print(sum(40,total))

#clean code
