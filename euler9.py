#python programing questions No.9
#a pythagorean triplet is a set of three natural numbers, a< b <c, for which,
# a^2 + b^2 = c^2
#for example, 3^2 + 4^2 = 9 +16 = 25 =5^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000
#find the product abc

#version 0.1
import random
import math

inta =0
intb =0
intc =0

sum0 =0
product0 =0

intz =1000

while True:
	intc=math.sqrt(inta*inta +intb*intb)
	sum0 =inta +intb +intc
	if sum0 ==1000:
		break
	else:
		inta= random.randint(1, 1000)
		intb= random.randint(1,1000)
		print inta
		print intb
		print intc
	print('----------')
	

product0 = inta*intb*intc

print('The product of abc of a+b+c=1000 is: ' +str(product0))
print('a: ' +str(inta))
print('b: ' +str(intb))
print('c: ' +str(intc))

