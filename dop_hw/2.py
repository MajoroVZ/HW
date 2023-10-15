def next_max_int(n):
    b = n
    for i in range(len(n)-1, -1, -1):
        k = n[i]
        if int(n[i]) > int(n[i-1]):
            n = n.replace(n[i], n[i-1],1)
            n = n.replace(n[i-1], k,1)
            break
    if n == b:
        return -1
    return n

n = str(input())
print(next_max_int(n))
#1241