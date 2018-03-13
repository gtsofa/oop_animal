# Animal class

class Animal:
    """
    preceding variable with __ makes them private that means
    if we want to use them we first need to create a function in this class
    """
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    # constructor
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound


    # set setter & getter for all the variables. 

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(slef, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    