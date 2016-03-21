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
        self.printInfo(addr, hit)

    def printInfo(self, addr, hit):
        if hit:
            print("access " + str(addr) + " (H) " + ":"),
        else:
            print("access " + str(addr) + " (M) " + ":"),
        for i in self.history:
            print(i[0]),
        print("")

if __name__ == '__main__':
    visit_seq = ['a', 'd', 'e', 'c', 'c', 'd', 'b', 'c', 'e', 'c', 'e', 'a', 'd']
    print("------- Woring Set -------")
    ws = WorkingSet(4)
    for addr in visit_seq:
        ws.access(addr)
