
def passMatch(numStr, p1=True):
    if any(numStr[i] > numStr[i+1] for i in range(5)):
        return 0
    else:
        intMap = [numStr.count(n) for n in set(numStr)]
        if p1:
            if any(intM >= 2 for intM in intMap):
                return 1
            else:
                return 0
        else:
            if any(intM == 2 for intM in intMap):
                return 1
            else:
                return 0


print('PART1 {}'.format(sum([passMatch(str(num)) for num in range(372037,905157+1)])))
print('PART1 {}'.format(sum([passMatch(str(num), p1=False) for num in range(372037,905157+1)])))




