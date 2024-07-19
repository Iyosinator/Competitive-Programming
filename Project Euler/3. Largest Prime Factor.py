'''
Problem Link:- https://projecteuler.net/problem=3
Title:- Largest Prime Factor
Problem Statement:-
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


largest_prime_factor(600851475143)
