from collections import defaultdict

input = 'inputD3'
def readCoord(input):
    arr = [i.strip() for i in open(input)]
    return arr

arrs=readCoord(input)
cirBoard = defaultdict(lambda:defaultdict(int))
dirMap = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
for i, arr in enumerate(arrs):
    makeKey = 'w'+str(i)
    step=x =y= 0
    for w in arr.split(','):
        getDir, getSteps = w[0], int(w[1:])
        x_, y_ = dirMap[getDir]
        for i in range(getSteps):
            x += x_
            y += y_
            step += 1
            cirBoard[(x,y)][makeKey] += step

interSect = []
minStep = []
for k, v in cirBoard.items():
    if len(v) == 2:
        x, y = k
        interSect.append(abs(x)+abs(y))
        minStep.append(v.get('w1') + v.get('w0'))
print('Least Distance {}'.format(min(interSect)))
print('Least Steps {}'.format(min(minStep)))

