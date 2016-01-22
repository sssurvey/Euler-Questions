#euler problem 16
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
#what is the sum of the number 2^1000
import math

powerCap = 1000
number = 2
finalNum = 0
numList = []
sum0 = 0


finalNum = int(math.pow(number,powerCap))
numList = [int(i) for i in str(finalNum)]

for i in range(0, len(numList)):
	sum0 += numList[i]

print ("The ans is: "+str(sum0))