'''
Problem: 5. Smallest Multiple
Title: Smallest Multiple
Problem Statement:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def smallest_multiple(n):
    from math import gcd
    def lcm(a, b):
        return a * b // gcd(a, b)
    ans = 1
    for i in range(2, n + 1):
        ans = lcm(ans, i)
    return ans


smallest_multiple()