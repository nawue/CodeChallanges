# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?
#
import math

num = 600851475143

factors = []
i = 2
while num > 1:
    if num % k == 0:
        num = num / k
        factors.append[k]
    else:
        k+=1
print(max(factors))
