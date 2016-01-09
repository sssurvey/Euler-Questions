#python programing questions No.10
#the sum of the primes below 10 is 2 + 3 +5 + 7 =17
#find the sum of all the primes below two million?

#version 0.1
def isPrime(number):
	for i in range(2, number):
		if (number %i) ==0:
			return False
	return number

def primeCounter(number,loopCounter):
	counter0 =0
	primeNumbers= []
	int0 =2
	int1 =0
	counter =loopCounter
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
		print('Calculating time remaining: ' +str(counter))
		counter =counter-1
		counter0 =counter0 +1
		if counter0 ==loopCounter:
			return primeNumbers
			break

#first arg will always larger then second one
#i set 999999999 as the prime number counter, 2000000-1 is the loop counter
#999999999 will never be reached if i set the loop counter is 2 mil, 999999999 is just because i was using one of my old functions from euler00007.py

primeNumbers =primeCounter(99999999,1999999)#first arg will always larger then second one
answer0 =sum(primeNumbers)
print('The sum of all the primes below two million: ' +str(answer0))

#need about 45 mins to finish the calculation
'''-------------------------------------------------------------------------------------------------------'''