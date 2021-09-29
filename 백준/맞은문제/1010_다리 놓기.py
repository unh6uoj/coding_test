import math

l = []
for i in range(int(input())):
    n, m = input().split()
    n = int(n)
    m = int(m)
    l.append(int(math.factorial(m) / (math.factorial(m-n) * math.factorial(n))))

for i in l:
    print(i)
