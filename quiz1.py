import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

for i in range(length,0,-1):
    subLength = i
    print('subLength' , subLength)
    needBreak = False
    if subLength==1:
        L_3 = L[0]
    else:
        currentIndex = 0
        while currentIndex+subLength<=length:
            j = currentIndex
            tempList = []
            tempList_sorted = []
            print('length', length)
            print('currentIndex', currentIndex)
            print('currentIndex+subLength', currentIndex + subLength)
            print('j', j)
            for j in range(currentIndex, currentIndex+subLength, +1):
                tempList.append(L[j])
            print('tempList', tempList)
            tempList_sorted=sorted(tempList)
            print('tempList_sorted', tempList_sorted)
            noGap = True
            for k in range(len(tempList_sorted)-1):
                if(tempList_sorted[k+1]-tempList_sorted[k]>1):
                    noGap = False
            if noGap:
                L_3 = tempList
                needBreak = True
                break
            else:
                currentIndex+=1
    if needBreak:
        break
    else:
        continue

print('L_3', L_3)
