x = int(input())
y = int(input())
k = 0
for i in range(x,y+1):
    if i % 5 ==0:
        k += i
print(k)
