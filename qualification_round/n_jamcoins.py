import sys

test_cases_num = int(sys.stdin.readline())

for test_case in range(test_cases_num):
    N = sys.stdin.readline().strip()
    A = int(''.join(['1' if int(char) == 4 else '0' for char in N]))
    N = int(N)
    B = N - A
    print("Case #{}: {} {}".format(test_case + 1, A, B), file=sys.stdout)
    sys.stdout.flush()