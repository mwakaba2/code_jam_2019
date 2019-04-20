import sys

test_cases_num = int(sys.stdin.readline())

for test_case in range(test_cases_num):
    N = int(sys.stdin.readline().strip())
    lydia = sys.stdin.readline().strip()
    lydia_path = (0, 0)

    my_path = ''
    curr = (0, 0)
    same_before = True

    for i in range(len(lydia)):
        m_x, m_y = curr
        x, y = lydia_path
        x, y = (x + 1, y) if lydia[i] == 'E' else (x , y + 1)
        if same_before:
            if m_x + 1 != x and m_x + 1 < N:
                my_path += 'E'
            else:
                my_path += 'S'
            same_before = False
        else:
            if m_x + 1 == x and m_x + 1 < N:
                my_path += 'E'
                same_before = True
            else:
                my_path += 'S'
                same_before = True
        curr = (m_x + 1, m_y) if my_path[-1] == 'E' else (m_x, m_y + 1)
        lydia_path = (x, y)

    print("Case #{}: {}".format(test_case + 1, my_path), file=sys.stdout)
    sys.stdout.flush()