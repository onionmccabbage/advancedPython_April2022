from threading import Thread
import time
import sys
import random
from timeit import default_timer # stonkingly good tool to measure time performance

def myFunc(name):
    for i in range(1,50):
        time.sleep(random.random()*0.1)
        sys.stdout.write(name) # or print()

if __name__ == '__main__':
    s = default_timer()
    # sequential execution takes about ten seconds
    # myFunc('a')
    # myFunc('b')
    # myFunc('c')
    # myFunc('d')
    # now lets try with threads - takes about 3 seconds to run four threads
    t1 = Thread(target=myFunc, args=('t1',) ) # Thread is a thread accessor - not the thread itself
    t2 = Thread(target=myFunc, args=('t2',) )
    t3 = Thread(target=myFunc, args=('t3',) )
    t4 = Thread(target=myFunc, args=('t4',) )
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    print('waiting for threads to (re)join the main thread...')
    t1.join() # very good practice to join threads as soon as you can
    t2.join()
    t3.join()
    t4.join()
    e = default_timer()
    print('total time was {}'.format(e-s))