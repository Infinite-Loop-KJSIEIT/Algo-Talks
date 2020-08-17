n = int(input())
a = list(map(int, input().strip().split()))
b = [a[i] for i in range(n)]
b.sort()
i, ans, a1 = 0, 0, []
for i in range(n):
    if a[i] != b[i]:
        ans += 1
        a1.append(i+1)
if ans == 2:
    print("yes")
    print("swap", a1[0], a1[1])
else:
    i, ans, t, d = 0, "yes", [], []
    while i < n:
        while i-1 < n and a[i] > a[i+1]:
            t.append(a[i])
            d.append(i)
            i += 1
        if len(t) == 0:
            i += 1
            continue
        t.append(a[i])
        d.append(i)
        break
    a[d[0]:d[len(d)-1]+1] = t[::-1]
    # print(a)
    if a == b:
        print("yes")
        print("reverse", d[0]+1, d[len(d)-1]+1)
    else:
        print("no")
