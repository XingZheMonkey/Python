class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def io(self):
        return f'{self.name} 是个乖狗狗'

baby=Dog("贝贝",1,23)

print (f'姓名: {baby.name}')
print (f'年龄: {baby.age}')
print (f'io: {baby.io()}')