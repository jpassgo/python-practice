# 
# 204. Count Primes
# 
# Given an integer n, return the number of prime numbers that are strictly less than n.
# 
# https://leetcode.com/problems/count-primes/
# 

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = []
        for i in range(n):
            if i == 2:
                primes.append(i)
            if(i % 2 != 0 
                and not self.modulo(i, 3)
                and not self.modulo(i, 5)
                and not self.modulo(i, 7)
                and not self.modulo(i, 11)
                and not self.modulo(i, 13)):                    
                    primes.append(i)

        return primes


    def modulo(self, n, modulo):
        if n == modulo:
            return False
        else:
            return n % modulo == 0  




solution = Solution()
primes = solution.countPrimes(100)
[print(f'{prime} ', end='') for prime in primes]
