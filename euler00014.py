#euler question 14

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


