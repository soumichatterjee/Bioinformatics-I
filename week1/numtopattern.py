invmap = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

def numbertopattern(index, k):
    if k == 1:
        return invmap[index]
    patterncollect = ''
    while index != 0:
        patterncollect = invmap[index % 4] + patterncollect
        index = index // 4
        numbertopattern (index, k)
    if len(patterncollect) < k:
        patterncollect =  (k - len(patterncollect))*'A' + patterncollect
        return patterncollect

print numbertopattern(5699,7)