#superlist

class SuperList(list):
    def __len__(self):
        return 1000
    
sl1 = SuperList()

print(len(sl1))
sl1.append(66)
sl1.append(662)
sl1.append(6635)
print(sl1[2])

print(issubclass(SuperList, list))
print(issubclass(list, object))