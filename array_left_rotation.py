def array_left_rotation(a, n, k):
    newarray = a[k:]
    newarray.extend(a[:k])
    return newarray


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')