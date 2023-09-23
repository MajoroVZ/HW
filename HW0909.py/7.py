x = float(input())
y = float(input())
k = 0
for i in range(int(x), int(y) + 1):
    if i % 5 == 0:
        k += i
print(k)
