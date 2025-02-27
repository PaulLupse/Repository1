from functools import cmp_to_key

lista = [12312, 234, 5666, 222, 1111, 11111, 1000000000, 5, 666, 'aAAAAAAaccs']

def compare(a, b):
    cpa = a; sum_a = 0; cpb = b; sum_b = 0
    try:
        while cpa:
            sum_a += cpa % 10
            cpa //= 10
    except:
        cpa = a.lower()
        while cpa:
            sum_a += ord(cpa[0]) - ord('a') + 1
            cpa = cpa[1::]

    try:
        while cpb:
            sum_b += cpb % 10
            cpb //= 10
    except:
        cpb = b.lower()
        while cpb:
            sum_b += ord(cpb[0]) - ord('a') + 1
            cpb = cpb[1::]

    if sum_a < sum_b:
        return 1
    elif sum_a == sum_b: return 0
    else: return -1

print(sorted(lista, key = cmp_to_key(compare)))


