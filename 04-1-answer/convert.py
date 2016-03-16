def load_data(path):
    f = open(path)
    txt = f.read()
    pages_txt = txt.split("\n")
    pages = []
    for each in pages_txt:
        if len(each.strip()) == 0:
            continue
        data = each[9:]
        page_id = eval("0x" + each[5:7])
        each_data = data.split()
        all_data = map(lambda x: eval("0x" + x), each_data)
        pages.append(all_data)
    return pages

mem = load_data("04-1-answer/mem.txt")
disk = load_data("04-1-answer/disk.txt")
pdbr = 0xd80 / 32

def query_loop():
    while True:
        query = raw_input('input hex addr to query or q to exit\n')
        if query[0] == 'q' or query[0] == "Q":
            return
        try:
            addr = eval("0x" + query)
        except Exception, e:
            print "invalid query"
            continue
        if addr >= 32 * 1024:
            print "addr overflow"
            continue
        pde_index = addr / 1024
        pte_index = addr / 32 % 32
        offset = addr % 32

        pde = mem[pdbr][pde_index]
        if pde < 128:
            print "invalid pde"
            continue
        pde -= 128
        print "pde valid 1, pfn", hex(pde)

        pte = mem[pde][pte_index]
        if pte < 128:
            print "pte valid 0, pfn", hex(pte)
            print "disk sector address =", hex(pte * 32 + offset)
            print "value =", hex(disk[pte][offset])
        else:
            pte -= 128
            print "pte valid 1, pfn", hex(pte)
            print 'physical address =', hex(pte * 32 + offset)
            print 'value =', hex(mem[pte][offset])

if __name__ == "__main__":
    query_loop()
