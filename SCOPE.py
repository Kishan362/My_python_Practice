#scope - what variables do i have access to ?

a = 1


# def papavariable():
#     a = 10    
#     def confusius():
#      return sum
#     return confusius


# print(papavariable())
# print(a)

#1-starts with local
#2-parant local
#3-Global local
#4-built in python

#global variable
total = 0
def count(total):
    total += 1
    return total



print(count(count(count(total))))

#