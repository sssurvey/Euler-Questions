#euler question 14

#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.




#version 0.1
def eqEven(number):
	#n -> n/2
	sum0 = number/2
	return sum0


def eqOdd(number):
	#n -> 3n +1
	sum0 = 3*number + 1
	return sum0

'''-----------------------------------------------------------'''
number = 1000000
lengthOfS = 1
firstNum = 13
firstNumbk = 13
currentLongest = 0

while firstNumbk < number:
	if firstNum %2 > 0:
		firstNum = eqOdd(firstNum)
		lengthOfS += 1

	if firstNum %2 == 0:
		firstNum = eqEven(firstNum)
		lengthOfS += 1

	if firstNum == 1:
		lengthOfS += 1
		if lengthOfS > currentLongest:
			currentLongest = lengthOfS
			print('This is the number: ' + str(firstNumbk))
		firstNumbk +=1
		firstNum = firstNumbk
		lengthOfS = 0


