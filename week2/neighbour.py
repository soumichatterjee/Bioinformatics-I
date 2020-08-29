def hamming( patternA, patternB ):
    hamDistance = 0
    for i in range(len(patternA)):
        if patternA[i] != patternB[i]:
            hamDistance+=1
    return hamDistance

def neighbours( s, d ):
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbour in neighbours(s[1:],d):
        if hamming(s[1:],neighbour) < d:
            out.extend(['A'+neighbour,'C'+neighbour,'G'+neighbour,'T'+neighbour])
        else:
            out.append(s[0] + neighbour)
    return out

x = neighbours('ACACCATGA', 3)
for i in x:
    print i,