#project euler 13


listOfD =[]
sum0 =0
with open("euler00013file.txt", 'r') as fobj:
    for line in fobj:
        numbers = [int(x) for x in line.split()]
        sum0 = numbers[0] + sum0

print('The answer is: ' +str(sum0))
