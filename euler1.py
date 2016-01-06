#python programing questions No.1
#Multiples of 3 and 5
#if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
#find the sum of all the multiples of 3 or 5 below 1000

#version 0.1
st0 ="The sum of multiples of 3 or 5 below 1000 sum: "
int0 =3
int1 =5

m0 =1
m1 =1


for int0 in range(0,1000): 
    int0 =int0 *m0
    m0 =m0+1
for int1 in range(0,1000):
    int1 =int1 *m1
    m1 =m1+1

sum0= int0 +int1 

print(st0 +str(sum0))

'''---------------------------------------------------------------------------------'''
#version 0.2
