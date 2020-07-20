arr=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]
    
def P1(arr, noun, verb, silent=False):
    arr[1] = noun
    arr[2] = verb
    n = 0
    while n < len(arr)-3:
        pos1 = arr[n+1]
        pos2 = arr[n+2]
        outP = arr[n+3]
        if arr[n] == 1:
            arr[outP]=arr[pos1]+arr[pos2]
            n += 4
        elif arr[n] == 2:
            arr[outP] = arr[pos1]*arr[pos2]
            n += 4
        else:
            break
    if not silent:
        print('The Zero Position is {}'.format(arr[0]))
    return arr[0]

P1(arr, noun = 12, verb=2, silent=True)

outP = 19690720
for n in range(0, 99):
    for v in range(0, 99):
        arr=[1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0]
        tempOut = P1(arr, noun = n, verb=v, silent=True)
        if tempOut == outP:
            print(n, v, 100*n+v)
            break
            
            





#if __name__ == "__main__":main()


