import math

to_len, a, b = input().split()

to_len = int(to_len)
a = int(a)
b = int(b)

count = 1
while to_len > 2:
    if a % 2 == 1 and b - a == 1:
        print(count)
        break

    a = math.ceil(a / 2)
    b = math.ceil(b / 2)
    to_len = int(to_len / 2)

    count += 1
else:
    print(-1)