#!/usr/bin/python3
number = 1008
var1 = 888
var2 = 777

data = {'1000':var1,'1010':var2}

def test_range(n):
    if n in range(1000,1010):
        data['1000']+=1
        print(data['1000'])
    elif n in range(1010,1020):
        data['1010']+=1
        print(data['1010'])
    else :
        print("The number is outside the given range.")

test_range(number)
test_range(number+10)


#for i in range(0,10):
#    print(i)
