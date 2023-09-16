# Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе
# переданного типа и верните его из класса-фабрики


class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


class Dog(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str,
                 is_pet: bool = True):
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_pet = is_pet

    def __str__(self):
        if self.is_pet:
            return f'Dog {self.name} age: {self.age} yo, ' \
                   f'color: {self.color}, {self.breed} is a pet'
        return f'Dog {self.name} age: {self.age} yo, ' \
               f'color: {self.color}, breed: {self.breed} is wild'


class Horse(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 type: str,
                 trained: bool = True):
        super().__init__(name, age)

        self.type = type
        self.trained = trained

    def __str__(self):
        if self.trained:
            return f'Horse {self.name} age: {self.age} yo, ' \
                   f'type: {self.type}, knows commands'
        return f'Horse {self.name} age: {self.age} yo, ' \
               f'type: {self.type}, needs to be trained'


class Fish(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 water_kind: str):
        super().__init__(name, age)

        self.water_kind = water_kind

    def __str__(self):
        if self.water_kind:
            return f'Fish {self.name} age: {self.age} yo, ' \
                   f'needs sea water'
        return f'Fish {self.name} age: {self.age} yo, ' \
               f'needs pure water'


class Factory:
    def create_animal(self, animal_type, **kwargs):
        if animal_type == 'Dog':
            return Dog(**kwargs)
        elif animal_type == 'Horse':
            return Horse(**kwargs)
        elif animal_type == 'Fish':
            return Fish(**kwargs)
        else:
            raise ValueError('Unsupported animal type')


if __name__ == '__main__':
    animal_factory = Factory()

    animal_1 = animal_factory.create_animal('Dog', name='Fluffy', age=3,
                                            color='cream', breed='multiepoo',
                                            is_pet=True)
    print(animal_1)

    animal_2 = animal_factory.create_animal('Horse', name='Plotva',
                                            age=2, type='riding horse',
                                            trained=True)
    print(animal_2)

    animal_3 = animal_factory.create_animal('Fish', name='Nemo',
                                            age=1, water_kind='sea water')
    print(animal_3)