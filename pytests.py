import pytest

from factory import Animal, Dog, Horse, Fish, Factory  # Замените "your_module" на имя вашего модуля

@pytest.fixture
def animal_factory():
    return Factory()

def test_create_dog(animal_factory):
    animal = animal_factory.create_animal('Dog', name='Fluffy', age=3, color='cream', breed='multiepoo', is_pet=True)
    assert isinstance(animal, Dog)
    assert animal.name == 'Fluffy'
    assert animal.age == 3
    assert animal.color == 'cream'
    assert animal.breed == 'multiepoo'
    assert animal.is_pet

def test_create_horse(animal_factory):
    animal = animal_factory.create_animal('Horse', name='Plotva', age=2, type='riding horse', trained=True)
    assert isinstance(animal, Horse)
    assert animal.name == 'Plotva'
    assert animal.age == 2
    assert animal.type == 'riding horse'
    assert animal.trained

def test_create_fish(animal_factory):
    animal = animal_factory.create_animal('Fish', name='Nemo', age=1, water_kind='sea water')
    assert isinstance(animal, Fish)
    assert animal.name == 'Nemo'
    assert animal.age == 1
    assert animal.water_kind == 'sea water'

def test_create_unknown_animal(animal_factory):
    with pytest.raises(ValueError):
        animal_factory.create_animal('UnknownAnimal', name='Unknown', age=0)
