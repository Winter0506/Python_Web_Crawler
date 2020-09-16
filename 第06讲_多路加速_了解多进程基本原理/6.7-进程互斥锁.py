from multiprocessing import Process, Lock
import time

class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            # self.lock.acquire()
            print(f'Pid: {self.pid} LoopCount: {count}')
            # self.lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(100,150):
        p = MyProcess(i, lock)
        p.start()
# 我没出现问题啊