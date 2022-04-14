# semaphores can pass messages e.g. to count how many accessors to a data source
from threading import Thread, BoundedSemaphore, Lock
import time
from timeit import default_timer

sem = BoundedSemaphore(3) # we can control how many concurrent accessors are permitted

class MyClass:
    def __call__(self, name):
        global sem
        sem.acquire()
        time.sleep(3)
        sem.release()

def main():
    m1 = MyClass()
    m2 = MyClass()
    m3 = MyClass()
    m4 = MyClass()
    s = default_timer()
    t1 = Thread(target=m1, args=('A',))
    t2 = Thread(target=m2, args=('B',))
    t3 = Thread(target=m3, args=('C',))
    t4 = Thread(target=m4, args=('D',))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    e = default_timer()
    print('total time {}'.format(e-s))

if __name__ == '__main__':
    main()