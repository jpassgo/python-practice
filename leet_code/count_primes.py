# 
# 204. Count Primes
# 
# Given an integer n, return the number of prime numbers that are strictly less than n.
# 
# https://leetcode.com/problems/count-primes/
# 

# Check the last digit of the number, depending on what number it ends in run a modulo check with the corresponding modulo numbers.
# 
# 

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        for i in range(n):
            if(i % 2 != 0):
                remainder = str(i % 10)
                if(remainder == 1):
                    if(i % 11 != 0):
                        primes.append(i)
                elif(remainder == 3)

