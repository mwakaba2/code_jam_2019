import sys

test_cases_num = int(sys.stdin.readline())

for test_case in range(test_cases_num):
    A, B = (int(num) for num in sys.stdin.readline().strip().split(' '))
    low, high = A, B
    n = int(sys.stdin.readline().strip())
    while n > 0:
        guess = low + ((high-low) // 2)
        if guess == A:
            guess += 1
        print(guess, file=sys.stdout)
        sys.stdout.flush()
        verdict = sys.stdin.readline().strip()
        if verdict == 'TOO_BIG':
            high = guess - 1
        elif verdict == 'TOO_SMALL':
            low = guess + 1
        elif verdict == 'WRONG_ANSWER':
            exit()
        else:
            break
        n -= 1