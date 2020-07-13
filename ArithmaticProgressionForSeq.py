def canMakeArithmeticProgression(arr):
    arr.sort()
    diff = abs(arr[0] - arr[1])
    for i in range(2, len(arr)):
        if abs(arr[i-1]-arr[i]) != diff:
            return False
    return True
if __name__ == "__main__":
    print(canMakeArithmeticProgression([3,5,1]))
    print(canMakeArithmeticProgression([1,2,4]))
    print(canMakeArithmeticProgression([1,2]))
    print(canMakeArithmeticProgression([-30,0,-10,20,-20,10]))
    print(canMakeArithmeticProgression([11,7,5,9,3]))
    print(canMakeArithmeticProgression([-68,-96,-12,-40,16]))
