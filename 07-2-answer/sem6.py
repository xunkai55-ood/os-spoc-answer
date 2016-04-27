import threading
import time
import random


class Storage(object):

    def __init__(self, M, N):
        assert(M > 0 and N > 0)
        self.a_minus_b = threading.Semaphore(N)
        self.b_minus_a = threading.Semaphore(M)
        self.n = N
        self.m = M
        self.a = 0
        self.b = 0
        self.lock = threading.Lock()

    def check(self):
        assert(self.a >= 0 and self.b >= 0)
        assert(self.a - self.b <= self.n)
        assert(self.b - self.a <= self.m)

    def report(self):
        return "a=%d, b=%d" % (self.a, self.b)


class Good(threading.Thread):

    def __init__(self, storage):
        threading.Thread.__init__(self)
        self.storage = storage

    def run(self):
        for i in range(50):
            self.add()
            time.sleep(random.random())


class A(Good):

    def __init__(self,  storage):
        Good.__init__(self, storage)

    def add(self):
        # add a good
        self.storage.a_minus_b.acquire()
        self.storage.lock.acquire()
        self.storage.a += 1
        self.storage.check()
        print "+A", self.storage.report()
        self.storage.lock.release()
        self.storage.b_minus_a.release()


class B(Good):

    def __init__(self,  storage):
        Good.__init__(self, storage)

    def add(self):
        # add a good
        self.storage.b_minus_a.acquire()
        self.storage.lock.acquire()
        self.storage.b += 1
        self.storage.check()
        print "+B", self.storage.report()
        self.storage.lock.release()
        self.storage.a_minus_b.release()


if __name__ == "__main__":

    storage = Storage(2, 5)
    a = A(storage)
    b = B(storage)
    a.start()
    b.start()
