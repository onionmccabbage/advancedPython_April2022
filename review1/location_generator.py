# generate city/country pairs

def locationGen():
    locations = [
        ('Hull','uk'),
        ('Canberra','aus'),
        ('Berlin','de'),
        ('Madrid','es')
        ('Athlone','ie'),
        ('Galway','ie'),
    ]
    index = 0
    while index < len(locations):
        # instead of a return statement, we have a yield statement
        yield locations[index] # yields the next value in the sequence being generated
        index += 1

if __name__ == '__main__':
    inst = locationGen()
    print( inst.__next__() )
    print( inst.__next__() )
    print( inst.__next__() )