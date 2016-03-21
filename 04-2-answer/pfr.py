class PageFaultRate:
    def __init__(self, window_size):
        self.window_size = window_size
        self.history = []
        self.last_fault = 0
        self.current = -1
        self.mem = []

    def access(self, addr):
        self.history.append(addr)
        self.current += 1
        if len(self.history) > self.window_size + 1:
            del self.history[0]

        hit = True
        if addr not in self.mem:
            hit = False
            delta = self.current - self.last_fault
            self.last_fault = self.current

            if delta <= self.window_size:
                self.mem.append(addr)
            else:
                new_mem = []
                for i in self.mem:
                    if i in self.history:
                        new_mem.append(i)
                self.mem = new_mem
                self.mem.append(addr)
        self.display(addr, hit)

    def display(self, addr, hit):
        print "H" if hit else "M", addr, "|| now:",
        for i in self.history:
            print i,
        print


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 2, 3, 3, 5, 4, 2, 1]
    print "------- Page Fault Rate -------"
    pfr = PageFaultRate(2)
    for index in seq:
        pfr.access(index)
