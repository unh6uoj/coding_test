h, m = input().split()

h = int(h)
m = int(m)

time = (h*60) + m
time -= 45

result = divmod(time, 60)
if result[0] == -1:
    print(23, result[1])
else:
    print(result[0], result[1])
