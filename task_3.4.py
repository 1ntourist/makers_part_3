l = input("Введите цифры через пробел: ").split()
l = list(map(lambda x: int(x), l))

def min_l(l):
    if max(l) <= 0:
        return 1
    for x in range(min(l), max(l)):
        for y in l:
            if x not in l:
                return x
    return max(l)+1
print(min_l(l))
