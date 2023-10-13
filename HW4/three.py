def f(x):
    b = True
    if len(x) > 1:
        for i in range(0, len(x)):
            for y in range(i+1, len(x)):
                if x[i] == x[y]:
                    b = False
                    break
    else:
        for u in range(len(x[0])):
            for q in range(u + 1, len(x[0])):
                if x[0][u] == x[0][q]:
                    b = False
    return b

if __name__ == "__main__":
    print(f(x = [a for a in input().split()]))
