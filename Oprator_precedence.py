# oprator precedence

# 20 + (3 * 4) =12
print((20 - 3)  + 5 ** 2)

# () first priority
# ** second priority
# * / third priority
# + - fourth priority
print('----------------------------')

#guess the output

print((5 + 4) * 10 / 2) #9*5 

print(((5 + 4) * 10) / 2) #90/2

print((5 + 4) * (10 / 2)) #9*5

print(5 + (4 * 10) / 2) #5+40/2

print(5 + 4 * 10 // 2) #5+20