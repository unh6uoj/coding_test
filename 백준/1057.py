N, kim, im = input().split()
N = int(N)
kim = int(kim)
im = int(im)

all_list = [0 for i in range(1, N+1)]
all_list[kim-1] = 1
all_list[im-1] = 1

print(all_list)

count = 0
while True:
    count += 1
    print(all_list)
    length = len(all_list)
    new_list = all_list
    for i in range(0, length, 2):
        print(i, all_list[i])
        try:
            if all_list[i] == 1:
                # del all_list[i+1]
                new_list.append(all_list[i])
            else:
                # del all_list[i]
                new_list.append(all_list[i+1])
        except:
            pass
    new_list = []

    if new_list.count(1) == 1:
        print(count)
        break
