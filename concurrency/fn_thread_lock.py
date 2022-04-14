from threading import Thread, Lock
import time
import sys
import random
from timeit import default_timer # stonkingly good tool to measure time performance

def main():
    # we need to aim for thread-safety, so shared resources must be locked for access
    lock = Lock() # we havea a lock!
    with lock: # this aquires the lock ofr us and re-cycles as needed
        for _ in range(1,50):
            time.sleep(random.random()*0.1)
            sys.stdout.write('{} '.format(_))
    # no need to lock.release() since the 'while' operator will release when done

if __name__ == '__main__':
    main()