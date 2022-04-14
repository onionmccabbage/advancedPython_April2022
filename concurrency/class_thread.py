from threading import Thread
import time
import sys
import random
from timeit import default_timer # stonkingly good tool to measure time performance

class MyThread(Thread): # our class inherits everything fro mthe Thread class
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    # Threads have a 'run' method which we can override
    def run(self):
        for i in range(1,50):
            time.sleep(random.random()*0.1)
            sys.stdout.write(self.name)

if __name__ == '__main__':
    s = default_timer()
    m1 = MyThread('m1')
    m2 = MyThread('m2')
    m3 = MyThread('m3')
    m4 = MyThread('m4')
    m1.start()
    m2.start()
    m3.start()
    m4.start()
    m1.join()
    m2.join()
    m3.join()
    m4.join()
    e = default_timer()
    print('total time was {}'.format(e-s))
