class PageFaultRate:
    def __init__(self, window_size):
        self.window_size = window_size
        self.cache = []
        self.last_fault = 0
        self.current = -1
        self.mem = set()

    def access(self, addr):
        self.cache.append(addr)
        self.current += 1
        if len(self.cache) > self.window_size + 1:
            self.cache = self.cache[1:]
        hit = True
        if addr not in self.mem:
            hit = False
            delta = self.current - self.last_fault
            self.last_fault = self.current

            if delta <= self.window_size:
                self.mem.add(addr)
            else:
                new_mem = set()
                for i in self.cache:
                    if i in self.mem:
                        new_mem.add(i)
                self.mem = new_mem
                self.mem.add(addr)
        self.display(addr, hit)

    def display(self, addr, hit):
        print "H" if hit else "M", addr, "|| now:",
        for i in self.cache:
            print i,
        print


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 2, 3, 3, 5, 4, 2, 1]
    print "------- Page Fault Rate -------"
    pfr = PageFaultRate(2)
    for index in seq:
        pfr.access(index)
