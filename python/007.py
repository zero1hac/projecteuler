if __name__ == "__main__":
    isPrime = [True]*1000001
    i = 2
    while i <= 1000:
        if isPrime[i]:
            k = 0
            while i*i + i*k<=1000000:
                isPrime[i*i + i*k] = False
                k+=1
        i+=1
    count = 0
    i = 2
    while True:
        if isPrime[i]:
            count+=1
            if count==10001:
                break
        i+=1
    print(i)