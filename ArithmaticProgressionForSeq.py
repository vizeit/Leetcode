def canMakeArithmeticProgression(arr):
    minval = float('inf')
    maxval = -float('inf')
    total = 0
    for item in arr:
        if item < minval:
            minval = item
        if item > maxval:
            maxval = item
        total+=item
    return total == (len(arr)*(minval+maxval))//2 and not (len(arr)*(minval+maxval))%2
if __name__ == "__main__":
    print(canMakeArithmeticProgression([3,5,1]))
    print(canMakeArithmeticProgression([1,2,4]))
    print(canMakeArithmeticProgression([1,2]))
    print(canMakeArithmeticProgression([-30,0,-10,20,-20,10]))
    print(canMakeArithmeticProgression([11,7,5,9,3]))
    print(canMakeArithmeticProgression([-68,-96,-12,-40,16]))
