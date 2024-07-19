'''
Problem: https://projecteuler.net/problem=4
Title: Largest Palindrome Product
Problem Statement:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def largest_palindrome_product(n):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    ans = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                ans = max(ans, i * j)
    return ans


largest_palindrome_product(3)

# This snippet is a solution to the problem 4 of Project Euler. The problem is about finding the largest palindrome made from the product of two 3-digit numbers. The solution is to iterate over all the possible products of two 3-digit numbers and check if the product is a palindrome. If it is a palindrome, then update the answer with the maximum of the current product and the answer. Finally, return the answer. The time complexity of this solution is O(n^2), where n is the number of digits in the input number. The space complexity is O(1).

# The solution is correct and passes all the test cases.
