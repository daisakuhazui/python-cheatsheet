# -*- coding:utf-8 -*-
def dig_pow(n: int, p: int) -> int:
    """
    Some numbers have funny properties.

    For examples:
        89 --> 8¹ + 9² = 89 * 1
        695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
        46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

    Given a positive integer n written as abcd... (a, b, c, d... being digits)
    and a positive integer p
    we want to find a positive integer k, if it exists,
    such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

    In other words:
        s there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

    If it is the case we will return k, if not return -1.
    Note: n and p will always be given as strictly positive integers.
    """
    s = str(n)

    value = 0
    for i in range(0, len(s), 1):
        v= s[i: i+1]
        value += int(v) ** p
        p += 1

    r = value / n
    print(r)
    if r.is_integer():
        return r
    return -1

