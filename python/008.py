if __name__ == "__main__":
    file_ = open('../data/008.txt','r')
    number = file_.readline().strip()
    len_ = len(number)
    prev = 1
    prod = 1
    max_prod = 1
    i = 0
    while i<13:
        prod *= int(number[i])
        i+=1
        max_prod = max_prod > prod and max_prod or prod
    while i<len_:
        prod /= int(number[i-13])
        prod *= int(number[i])
        i+=1
        max_prod = max_prod > prod and max_prod or prod
    print(max_prod)
