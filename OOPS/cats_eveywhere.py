#oop 

class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says meow')


    def oldest_cat(*args):
            older_cat = max(args)
            
            return older_cat




mini1=cat('Meeni',12) 
mini2=cat('Romeo',22)
mini3=cat('Tuffy',32)

mini1.meow()
oldest_cat_age = cat.oldest_cat(mini1.age,mini2.age,mini3.age)

oldest_cat_name = ""
for cat_instance in [mini1, mini2, mini3]:
    if cat_instance.age == oldest_cat_age:
        oldest_cat_name = cat_instance.name
        break
print(f"The oldest cat is {oldest_cat_name}")
