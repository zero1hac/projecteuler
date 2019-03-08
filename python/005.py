def  gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a*b/gcd(a,b)

if __name__ == "__main__":
    n = 20
    l = 1
    for i in xrange(2, n+1):
        l = lcm(l, i)
    print l
