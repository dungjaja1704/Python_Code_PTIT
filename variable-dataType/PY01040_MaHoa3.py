def Try(s):
    d = 0
    x = ""
    for i in s:
        d += ord(i) - ord("A")
    for i in s:
        x += chr(((ord(i) - ord("A") + d) % 26 + ord("A")))
    return x


t = int(input())
for k in range(t):
    s, x = input(), ""
    n = int(len(s) / 2)
    a, b = s[:n:], s[n::]
    a = Try(a)
    b = Try(b)
    for i in range(n):
        x += chr(((ord(a[i]) - 2 * ord("A") + ord(b[i])) % 26 + ord("A")))
    print(x)

