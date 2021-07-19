import math

# for i in range(int(input())):
# pass

jo = [0, 0, 3]
back = [0, 7, 4]

length = math.sqrt(math.pow(back[0]-jo[0], 2) + math.pow(back[1]-jo[1], 2))
length_a = length / 2
length_a = int(length_a)

good = abs(jo[2] - back[2])

print(length_a, good)

if good < length_a:
    print(2)
elif good > length_a:
    print(0)
elif good == length_a:
    print(1)
else:
    print(-1)
