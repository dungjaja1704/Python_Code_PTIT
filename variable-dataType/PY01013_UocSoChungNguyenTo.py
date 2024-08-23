from math import *
def nto(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        c = gcd(a, b)
        sum = 0
        while c > 0:
            sum += c % 10
            c //= 10
        if(nto(sum)):
            print("YES")
        else:
            print("NO")
        