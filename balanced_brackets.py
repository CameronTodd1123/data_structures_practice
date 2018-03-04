def is_matched(expression):
    pairs = {'{' : '}', '[' : ']', '(' : ')'}
    sk = []
    for c in expression:
        if c in pairs:
            sk.append(pairs[c])

        elif not sk or c != sk.pop(): #Note the not sk is True if len(sk) = 0
            return False
    return not sk


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")