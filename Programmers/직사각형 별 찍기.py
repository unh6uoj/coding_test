a, b = map(int, input().strip().split(' '))

result = ''
for i in range(a):
    result += '*'

for i in range(b):
    print(result)
