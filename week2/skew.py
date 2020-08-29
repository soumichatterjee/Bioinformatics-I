def Skew(Pattern):
    Array = []
    for i in range(len(Pattern)+1):
        Array.append(0)
    for i in range(len(Pattern)):
        if Pattern[i] == 'C':
            Array[i+1] = Array[i]-1
        elif  Pattern[i] == 'G':
            Array[i+1] = Array[i]+1
        else:
            Array[i+1] = Array[i]
    return Array
Pattern = "GAGCCACCGCGATA"
print(Skew(Pattern))