from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print('Woof')
class Cat(Animal):
    def sound(self):
        print('Miaow')
class Bat(Animal):
    def sound(self):
        print('-----')
class Aardvark(Animal):
    def sound(self):
        print('grunt')

# a factory
class CreatureFactory():
    def make_sound(self, obj):
        return eval(obj)().sound()

if __name__ == '__main__':
    cf = CreatureFactory()
    cf.make_sound('Dog')    
    cf.make_sound('Cat')    
    cf.make_sound('Bat')    
    cf.make_sound('Aardvark')    