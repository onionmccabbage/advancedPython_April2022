from threading import Thread, RLock, Condition # rlock is a re-entrant lock
import time

# some globals
lock = RLock()
data_available = Condition(lock) # this will let us know when the rlock is free

class Stack(): # represents a stack of data we need to access
    def __init__(self):
        self.data = [] # our stack of data members
    def push(self, item):
        with lock: # manage the re-entrant lock
            self.data.append(item)
    def pop(self):
        with lock:
            item = self.data.pop()
        return item

# here is a producer
def producer():
    for n in range(1,5):
        data_available.acquire() # et hold of our re-entrant lock via the condition
        stack.push(n)
        data_available.notify_all()
        data_available.release()
        time.sleep(0.2)

# here is a consumer
def consumer():
    while True:
        data_available.acquire()
        data_available.wait()
        data = stack.pop()
        data_available.release()
        print('received {}'.format(data))
        if data == 4:
            break

def main():
    prod_thread = Thread(target=producer)
    cons_thread = Thread(target=consumer)
    prod_thread.start()
    cons_thread.start()
    prod_thread.join()
    cons_thread.join()
    print('all done')

if __name__ == '__main__':
    stack = Stack() # an instance of our stack
    main()