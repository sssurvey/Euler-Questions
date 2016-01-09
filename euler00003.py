#python programing questions No.3
#Largest prime facter
#The prime factor of 13195 are 5, 7, 13 and 29
#what is the largest prime factor of the number 600851475143

#version 0.1
import random
from fractions import gcd

#cited Pollard Rho
#https://comeoncodeon.wordpress.com
'''def pollardRho(number):
	if number %2 ==0:
		return 2
	n0 =random.randint(1, number -1)
	n1 =n0
	n2 =random.randint(1, number -1)
	n3 = 1
	while n3 ==1:
		n0 =((n0 *n0) %number +n2) %number
		n1 =((n1 *n1) %number +n2) %number
		n1 =((n1 *n1) %number +n2) %number
		n3 =gcd(abs(n0 -n1), number)
	return n3'''


#cited stackoverflow.com/questions/15347174
def prime_factors(n):
	i =2
	factors =[]
	while i *i <=n:
		if n %i:
			i +=1
		else:
			n //=1
			factors.append(i)
	if n >1:
		factors.append(n)
	return factors

print(prime_factors())

#known issue
#Traceback (most recent call last):
#  File "euler3.py", line 39, in <module>
#    print(prime_factors(13195))
#  File "euler3.py", line 34, in prime_factors
#    factors.append(i)
#MemoryError


'''-------------------------------------------------------------------------'''



