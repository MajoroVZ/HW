x = []
while True:
  n = input()
  x.append(n)
  if not n:
    break
x.sort(reverse = True)
print(''.join(x))
