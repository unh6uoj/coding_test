# 정수 N이 주어진다. N보다 크거나 같은 수 중에, K개의 서로 다른 숫자로 이루어진 수 중 가장 작은 수를 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 N과 K가 주어진다. N은 10^18보다 작거나 같은 자연수이다. K는 10보다 작거나 같은 자연수이다.
# 출략 : 첫째 줄에 문제의 정답을 출력한다.

# 예제 입력 : 47 1 -> 55
# 예제 입력 : 12364 3 -> 12411

import sys

N, K = sys.stdin.readline().split()
N = int(N)
K = int(K)

numbers = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}
is_exit = False
while True:
    for i in range(0, 10):
        numbers[i] = str(N).count(str(i))

    count = list(numbers.values())
    if count.count(0) == 10-K:
        print(N)
        break

    N += 1
