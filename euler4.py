#python programing questions No.4
#largest palindrome product
#a palindromic number reads the same both ways. the largest palindrome made from the product of two 2-digit numbers is 9009 =91 x99
#find the largest palindrome made from the product of two 3-digit numbers

#version 0.1
int0 =999
int1 =999
sum0 =0
#here i use one number as 999, the largest number in 3 digit
#the other number as 900, since i assume the 900 and above times int0 will give me an answer, so i ignore all the 3 digit number before 900
def findPali():
	for int0 in range(900,999):
		for int1 in range(900,999):
			sum0 =int1*int0
			if checkPali(sum0)==True:
				break
			else:
				int1 =int1 -1
		int0 =int0 -1

def checkPali(numberNeed):
	intList =list(str(numberNeed))
	#since its 999x999, the largest number will be 6 digits, so ill just compare the first 3 and last 3 digits to see if they are equal
	a =0
	b =len(intList)
	if intList[a] ==intList[b -1]:
		if intList[a+1] ==intList[b -2]:
			if intList[a+2] ==intList[b -3]:
				print intList
				return True
			else:
				return False
		else:
			return False
	else:
		return False


print(findPali())
print("The number above None is the answer")
print("This program can only do 3 digit product palindromic, example:")
print("999x999 = and check palindromic")
'''----------------------------------------------------------------------------------------------'''


	
