# semaphores can pass messages e.g. to count how many accessors to a data source
from threading import Thread, BoundedSemaphore, Lock
import time

sem = BoundedSemaphore(2) # we can copntrol how many concurrent accessors are permitted
