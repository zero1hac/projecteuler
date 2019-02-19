from __future__ import print_function

if __name__ == "__main__":
    first = 1
    second = 2
    temp = 3
    sum_ = 2
    while temp <= 4000000:
        if (temp & 1) == 0:
            sum_ += temp
        first = second
        second = temp
        temp = first + second
    print(sum_)
