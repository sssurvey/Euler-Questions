#python programing questions No.7
#By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime number is 13
#what is the 10001st prime number?



def isPrime(number):
	for i in range(2, number):
		if (number %i) ==0:
			return False
	return number

def primeCounter(number):
	primeNumbers= []
	int0 =2
	int1 =0
	counter =0
	while True:
		int1 =isPrime(int0)
		if int1 > 0:
			primeNumbers.append(int0)
			int0 =int0 +1
		elif len(primeNumbers) ==number:
			return primeNumbers
			break
		else:
			int0 =int0 +1
		print('Calculating...' +str(counter))
		counter =counter+1


primeNumbersFinal =primeCounter(10001)
theAns = primeNumbersFinal[10000]

print('The 10001st prime number is: ' +str(theAns))
#again, the program works, but its going to take a while, about 10 mins
'''----------------------------------------------------------------'''
