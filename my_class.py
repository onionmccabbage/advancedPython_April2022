# overriding built-ins
class AnyName: # implicitly inherit from 'object'
    def __init__(self): # __init__ is one of many 'dunder' items in python
        self.data = "ABCDEFG" # properties of each instance
    def __str__(self): # here we override how 'print' operates
        return 'Instance of AnyName class, which contains {}'.format(self.data)
    def __getitem__(self, id): # here we override iterable access
        return self.data[id]

# override equality
class Word:
    '''This class compares words regardless of case'''
    def __init__(self, text):
        self.text = text
    def __eq__(self, other_word): # __eq__ is the built in equality operator
        return self.text.lower() == other_word.text.lower()

# use with great care!!!!!!
# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__': # only run the following code if this is the main module
    # this bit does NOT run if this module is imported
    # create an instance of our class
    a = AnyName()
    print(a[3]) # D
    for _ in a:
        print(_, end='-')
    h = 'hello'
    j = 'Hello'
    w = Word(h)
    x = Word(j)
    print(w == x) # True