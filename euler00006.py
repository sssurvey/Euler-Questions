#python programing questions No.6
#sum square difference
#The sum of the squares of the first ten natural number is,
#1^2 + 2^2 + ... +10^2 =385
#The square fo the sum of the first ten natural numbers is,
#(1+2+3+....+10)^2 =55^2 =3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640
#find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#version 0.1
def squareOfsum():
	int0 =1
	sum0 =0
	ans0 =0
	for i in range(0,100): #(1+2+....+n)^2
		sum0 =sum0 +(int0)
		int0 =int0 +1

	ans0 =sum0*sum0
	return ans0


def sumOfSquare():
	int0 =1
	sum0 =0
	ans0 =0
	for i in range(0,100): #1^2 + 2^2 + ... +n^2
		sum0= sum0 +(int0)*(int0)
		int0= int0 +1
	return sum0

squareOfsum =squareOfsum()
sumOfSquare =sumOfSquare()

print('(1+2+....+100)^2 is equal to: ' +str(squareOfsum))
print('1^2 + 2^2 + ... +100^2 is equal to: ' +str(sumOfSquare))
print('The difference between them is: ' +str(squareOfsum-sumOfSquare))
'''----------------------------------------------------------------------------------------'''
