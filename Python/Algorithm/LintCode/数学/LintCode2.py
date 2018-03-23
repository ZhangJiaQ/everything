'''
2. Trailing Zeros

Example
11! = 39916800, so the out should be 2

'''


def trailingZeros(n):
    # write your code here, try to do it without arithmetic operators.
    counter = 0
    i = 5
    while n//i >= 1:
        counter += n//i
        i = i * 5

    return counter
