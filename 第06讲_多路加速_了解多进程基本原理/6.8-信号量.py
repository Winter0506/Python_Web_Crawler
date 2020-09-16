from multiprocessing import Process, Semaphore, Lock, Queue
import time

buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()

class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()