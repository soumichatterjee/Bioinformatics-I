def FrequentWords(s,k,d):
    counts = {}
    for i in range(len(s)-k+1):
        for neighbour in neighbours(s[i:i+k],d):
            if neighbour not in counts:
                counts[neighbour] = 0
            counts[neighbour] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]

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

def hamming( patternA, patternB ):
    hamDistance = 0
    for i in range(len(patternA)):
        if patternA[i] != patternB[i]:
            hamDistance+=1
    return hamDistance
print(FrequentWords("TTTTTTCATCTCTATGTAATCTTTCATTTTTTCACTATGTAATCTCTATGTAATTCATTCAGTAAGTAAGTAATCTCTATTCTTTCATCTTTCATTCATCTTCTGTAATTTTTTTTTTTTCTATGTAATTCAGTAACTATTTTTGTAATCTTCTCTATTTTTTCTTCTTTCACTATTTCAGTAATCTCTATTTCACTATTCTTTCATTTTTTTTTTCACTATTTCACTATGTAAGTAATTCACTATCTATCTATTCTTTCATCTTCTCTATTTTTCTATCTATTTCACTATTTTTTCTTCTCTATCTATTCTTTTTCTATTTCACTATGTAA", 7, 2))