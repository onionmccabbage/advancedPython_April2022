class Person():
    '''inherits from object'''
    def __init__(self, n):
        self.__name = n # mangling - make it hard to access
    # get and set methods
    @property # getter (this is a decorator)
    def name(self):
        return self.__name
    @name.setter 
    def name(self, n):
        # we should validate the name is a non empty string
        if type(n)==str and n !='':
            self.__name = n
        else:
            pass # we could raise an exception

# we can create abstract base classes (ABC)
from abc import ABCMeta, abstractmethod, abstractproperty

class AbtractShape(): # this will be an abstract base class for other concrete classes
    __metaclass__ = ABCMeta
    @abstractmethod
    def __str__(self):
        pass
    @property
    @abstractmethod
    def name():
        pass # no body in the abstracts



if __name__ == '__main__':
    p = Person('Timnit')
    p.name = 'Ethel' # calls the setter method
    print(p.name) # calls the name getter method
