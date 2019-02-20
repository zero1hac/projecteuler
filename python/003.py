from __future__ import print_function

if __name__ == "__main__":
    num = 600851475143
    frac = 2
    while frac*frac <= num:
        while num%frac==0 and num!=frac:
            num /= frac
        frac+=1
    print(num)
