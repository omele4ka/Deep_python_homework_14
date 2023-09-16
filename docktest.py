from factory import Dog, Horse, Fish, Factory


class Factory:
    """
    A Factory class for creating instances of different animals.

    Usage:
    >>> animal_factory = Factory()

    Create a Dog instance:
    >>> animal_1 = animal_factory.create_animal('Dog', name='Fluffy', age=3, color='cream', breed='multiepoo', is_pet=True)
    >>> animal_1.__str__()
    'Dog Fluffy age: 3 yo, color: cream, multiepoo is a pet'

    Create a Horse instance:
    >>> animal_2 = animal_factory.create_animal('Horse', name='Plotva', age=2, type='riding horse', trained=True)
    >>> animal_2.__str__()
    'Horse Plotva age: 2 yo, type: riding horse, knows commands'

    Create a Fish instance:
    >>> animal_3 = animal_factory.create_animal('Fish', name='Nemo', age=1, water_kind='sea water')
    >>> animal_3.__str__()
    'Fish Nemo age: 1 yo, needs sea water'

    Attempt to create an unknown animal type:
    >>> animal_factory.create_animal('UnknownAnimal', name='Unknown', age=0)
    Traceback (most recent call last):
        ...
    ValueError: Unsupported animal type
    """

    def create_animal(self, animal_type, **kwargs):
        """
        Create an Animal object of specified type.

        :param animal_type: Type of Animal ('Dog', 'Horse' or 'Fish').
        :param **kwargs: Keyword arguments specific to the
        chosen Animal type.
        :return: an instance of the specified Animal type.
        :raises ValueError: if an unsupported Animal type is provided
        """

        if animal_type == 'Dog':
            return Dog(**kwargs)
        elif animal_type == 'Horse':
            return Horse(**kwargs)
        elif animal_type == 'Fish':
            return Fish(**kwargs)
        else:
            raise ValueError('Unsupported animal type')

if __name__ == '__main__':
    import doctest
    doctest.testmod()