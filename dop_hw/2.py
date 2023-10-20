def next_max_int(n):
    b = n
    max = 0
    min = 9
    maxindex = 0
    minindex = 0
    for i in range(len(n)):
        if int(n[i]) >= max:
            max = int(n[i])
            maxindex = i
        if int(n[i]) <= min:
            min = int(n[i])
            minindex = i

    for i in range(len(n)-1, -1, -1):
        k = [i]

        

n = str(input())
print(next_max_int(n))
#1243