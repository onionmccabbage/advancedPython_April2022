# import <path><package><module>
import a
# we can iherit from other classes
class Coder(a.Person):
    def __init__(self, n, lang):
        a.Person.__init__(self, n) # call parent init
        self.lang = lang # no mangling

# we can use our abstract base class
# to make concrete classes
class Shape(a.AbtractShape):
    def __init__(self, n):
        self.name = n # use setter method
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n
    def __str__(self):
        return 'This is {} made up of {} {}'.format(self.name, self.__dict__, self.__class__)

if __name__ == '__main__':
    c = Coder('Ada', 'python')
    print('We have {} who codes in {}'.format(c.name, c.lang))
    s = Shape('Grace')
    print(s)