#python programing questions No.5
#smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#what is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#version 0.1
int0 =4
int1 =0
dividerCounter =0
divider =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]




while True:
	int1 =int0 %divider[dividerCounter]
	print(int1)
	if int1 >0:
		int0 =int0+1 #integer increase on`e
		dividerCounter =0
	elif int1 ==0 and dividerCounter <19:
		dividerCounter =dividerCounter+1 #dividercounter increase one to test next divider

	elif int1 ==0 and dividerCounter ==19:
		print('done')
		print(int0)
		break

print('The number is: '+str(int0))
#the program works, but it will take awhile to run
#took me about 1 and a half hour
'''----------------------------------------------------------------------------'''





