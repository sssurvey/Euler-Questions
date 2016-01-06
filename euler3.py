#python programing questions No.3
#Largest prime facter
#The prime factor of 13195 are 5, 7, 13 and 29
#what is the largest prime factor of the number 600851475143

#version 0.1
import random

#cited Pollard Rho
def function(number):
	if number %2 ==0:
		return 2
	n0 =random.randint(1, number -1)
	n1 =n0
	n2 =random.randint(1, number -1)
	n3 = 1
	while g ==1:
		n0 =((n0 *n0) %number +n2) %number
		n1 =((n1 *n1) %number +n2) %number
		n1 =((n1 *n1) %number +n2) %number
		n3 =gcd(abs(n0 -n1), number)
	return n3

num0 =13195
primeNums =[2,3]
primeTemp =0`


