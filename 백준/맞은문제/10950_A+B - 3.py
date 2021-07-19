count = int(input())

temp_list = []
for i in range(count):
    a, b = input().split()
    a = int(a)
    b = int(b)

    temp_list.append([a, b])

for temp in temp_list:
    print(sum(temp))
