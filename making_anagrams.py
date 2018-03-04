def number_needed(a, b):
    a, b = list(a), list(b)
    a_vals = list(a)
    for i in a_vals:
        if i in b:
            a.remove(i)
            b.remove(i)
    return len(a) + len(b)

a = input().strip()
b = input().strip()

print(number_needed(a, b))