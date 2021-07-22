import math

T = int(input())
jo = []
back = []
for i in range(T):
    a = input().split()
    a = list(map(int, a))
    jo.append([a[0], a[1], a[2]])
    back.append([a[3], a[4], a[5]])


for i in range(T):
    distance = int(
        math.sqrt(math.pow(back[i][0]-jo[i][0], 2) + math.pow(back[i][1]-jo[i][1], 2)))

    good = abs(jo[i][2] + back[i][2])

    if good > distance:
        print(2)
    elif good < distance:
        print(0)
    elif good == distance:
        print(1)
    else:
        print(-1)
