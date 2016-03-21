class WorkingSet:
    def __init__(self, window_size):
        self.window_size = window_size
        self.cache = []
        self.clock = -1

    def access(self, addr):
        self.clock += 1
        hit = False
        for i in range(len(self.cache)):
            if self.cache[i][0] == addr:
                del self.cache[i]
                hit = True
                break
        self.cache.append((addr, self.clock))
        i = 0
        while self.clock - self.cache[i][1] >= self.window_size and i < len(self.cache):
            i += 1
        self.cache = self.cache[i:]
        self.display(addr, hit)

    def display(self, addr, hit):
        print "H" if hit else "M", addr, "|| now:",
        for i in self.cache:
            print i[0],
        print

if __name__ == '__main__':
    seq = [1, 2, 3, 4, 2, 3, 3, 5, 4, 2, 1]
    print "------- Woring Set -------"
    ws = WorkingSet(4)
    for addr in seq:
        ws.access(addr)
