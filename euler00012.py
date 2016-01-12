#project euler 12

def makeTrian():
    number =4
    trian =0
    divider =1
    temp0 =0
    listOfD =[]
    sum0 =0

    for i in range(0,5):
        trian = number*(number+ 1)/2

        while True:
            temp0 =trian %divider #test if trian can be divided in to int
            print (temp0)

            if temp0 ==0:
                listOfD.append(divider)
                print('append')
            if temp0 !=0:
                print('do nothing to list, increase divider')

            divider =divider +1 #increase divider
            print(listOfD)


            if divider == trian and len(listOfD) < 5:
                listOfD.append(divider)
                print('Trian need increase--')
                break

            if len(listOfD)==5:
                sys.exit('x')






                '''if len(listOfD) ==5:
                    print('Done!')
                    for i in range(0, len(listOfD)):
                        sum0 =listOfD[i]+sum0
                        print(sum0)
                    print('finished')
                    print(listOfD)
                    print("number" +str(number))
                    sys.exit("done")

                '''


        print('test')
        listOfD =[]
        number =number +1

'''----------------------------------------------------------'''



print (makeTrian())
