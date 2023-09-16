import unittest
from factory import Factory, Dog, Fish, Horse


class TestFactory(unittest.TestCase):
    def setUp(self):
        self.animal_factory = Factory()

    def test_create_dog(self):
        animal = self.animal_factory.create_animal('Dog', name='Fluffy',
                                                   age=3, color='cream',
                                                   breed='multiepoo',
                                                   is_pet=True)
        self.assertIsInstance(animal, Dog)
        self.assertEquals(animal.name, 'Fluffy')
        self.assertEquals(animal.age, 3)
        self.assertEquals(animal.color, 'cream')
        self.assertEquals(animal.breed, 'multiepoo')
        self.assertTrue(animal.is_pet)

    def test_create_fish(self):
        animal = self.animal_factory.create_animal('Fish', name='Nemo',
                                                   age=1,
                                                   water_kind='sea water')
        self.assertIsInstance(animal, Fish)
        self.assertEquals(animal.name, 'Nemo')
        self.assertEquals(animal.age, 1)
        self.assertEquals(animal.water_kind, 'sea water')

    def test_create_horse(self):
        animal = self.animal_factory.create_animal('Horse',
                                                   name='Plotva',
                                                   age=2, type='riding horse',
                                                   trained=True)
        self.assertIsInstance(animal, Horse)
        self.assertEqual(animal.name, 'Plotva')
        self.assertEqual(animal.age, 2)
        self.assertEqual(animal.type, 'riding horse')
        self.assertTrue(animal.trained)

    def test_create_unknown_animal(self):
        with self.assertRaises(ValueError):
            self.animal_factory.create_animal('UnknownAnimal', name='Unknown', age=0)


if __name__ == '__main__':
    unittest.main()
