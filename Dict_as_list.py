# creating a dictionary as a list

class Dict_as_list:
    def __init__(self, dict):
        self.dict = dict
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dict):
            result = list(self.dict.values())[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
    def __index__(self,num):
        self.index = num
        self.index += num
        return self.index
        



# dict1 = {
#     'name': 'Kishan',
#     'age': 20,
#     'is_cool': True,
#     'fav_color': ['white', 'blue', 'black'],
#     123: [1,1,1],
#     True : 'Tomato',
#     True : 'Potato'
# }

dict1= {}
dict_as_list = Dict_as_list(dict1)

dict1(4)
dict_as_list.__index__('age')
print(dict_as_list.index)
print(dict1)