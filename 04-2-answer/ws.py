class WorkingSet:
    def __init__(self, window_size):
        self.window_size = window_size
        self.history = []
        self.time = -1

    def access(self, addr):
        self.time += 1
        hit = False
        for i in range(len(self.history)):
            if self.history[i][0] == addr:
                del self.history[i]
                hit = True
                break
        self.history.append([addr, self.time])
        while self.time - self.history[0][1] >= self.window_size:
            del self.history[0]
        self.display(addr, hit)

    def display(self, addr, hit):
        print "H" if hit else "M", addr, "|| now:",
        for i in self.history:
            print i[0],
        print

if __name__ == '__main__':
    seq = [1, 2, 3, 4, 2, 3, 3, 5, 4, 2, 1]
    print "------- Woring Set -------"
    ws = WorkingSet(4)
    for addr in seq:
        ws.access(addr)
