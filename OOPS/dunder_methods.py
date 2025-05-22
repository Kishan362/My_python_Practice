class toy ():
    def __init__(self, color, material, age):
        self.color = color
        self.material = material
        self.age = age
    def  __str__(self):
        return f'{self.color}'



action_figure = toy('red', 'plastic', 10)
print(action_figure.__str__())
print(action_figure.color)