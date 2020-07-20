import sys
import math

def getFuel(mass):
    out=math.floor((mass/3)-2)
    return out

def part1():
    inFile=sys.argv[1]
    arr = []
    total = 0
    with open(inFile) as inPut:
        for n in inPut:
            arr.append((int(n)))
            total += getFuel(int(n))
    print('PART1 >> TOTAL FUEL IS {}'.format(total))
    return arr

def recFuel(mass, total):
    out = getFuel(mass)
    if out < 0:
        return total
    else:
        total += out
        return recFuel(out, total)

def part2(arr):
    masTotal = 0
    for i in arr:
        total = 0
        masTotal += recFuel(i, total)
    print('PART2 >> TOTAL FUEL FOR FUEL IS {}'.format(masTotal))
    return masTotal

def main():
    arr=part1()
    part2(arr)


if __name__ == "__main__":main()
