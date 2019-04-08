import sys

test_cases_num = int(sys.stdin.readline().strip())


def get_primes(n):
    prime = [True] * (n + 1)
    primes = []
    num = 2

    while num * num <= n:
        if prime[num]:
            for i in range(num * 2, n + 1, num):
                prime[i] = False
        num += 1

    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)
    return primes


def in_values(sorted_lst, target):
    low, high = 0, len(sorted_lst) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        value = sorted_lst[mid]
        if value == target:
            return True
        if value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def get_selected_primes(prime_lst, min_p, max_p, sorted_lst):
    values_dictionary = {}
    final_primes = set()
    for i in range(len(prime_lst)):
        for j in range(i, len(prime_lst)):
            a, b = prime_lst[i], prime_lst[j]
            product = a * b
            if min_p <= product and product <= max_p:
                if in_values(sorted_lst, product):
                    values_dictionary[product] = (a, b)
                    final_primes.update({a, b})

    final_primes = list(final_primes)
    final_primes.sort()
    final_primes_dict = {}
    for i, num in enumerate(final_primes):
        final_primes_dict[num] = chr(65 + i)

    return values_dict, final_primes_dict


def get_decoded_text(values_lst, values_d, primes):
    text = ''
    not_used = ''
    for value in values_lst:
        a, b = values_d[value]
        char_a = primes[a]
        char_b = primes[b]
        if not not_used or char_a == not_used:
            text += char_a
            not_used = char_b
        else:
            text += char_b
            not_used = char_a

    # grab last character
    if char_a == not_used:
        text += char_a
    else:
        text += char_b

    return text


for test_case in range(test_cases_num):
    N, L = (int(num) for num in sys.stdin.readline().strip().split(' '))
    prime_list = get_primes(N)
    values = [int(num) for num in sys.stdin.readline().strip().split(' ')]
    sorted_values = sorted(values)
    min_product = min(values)
    max_product = max(values)
    values_dict, selected_primes = get_selected_primes(prime_list,
                                                       min_product,
                                                       max_product,
                                                       sorted_values)
    decoded_text = get_decoded_text(values, values_dict, selected_primes)
    print("Case #{}: {}".format(test_case + 1, decoded_text), file=sys.stdout)
    sys.stdout.flush()
