from math import ceil,sqrt
def prime(n1, n2):
    for i in range(n1, n2):
        is_prime = 0
        for j in range(2, ceil(sqrt((i)))):
            if i % j == 0:
                is_prime = 1
                break
        if is_prime:
            print(i)
            