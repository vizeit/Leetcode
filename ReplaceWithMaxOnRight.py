def replaceElements(arr):
    maxe=-1
    for i in range(len(arr)-1, -1, -1):
        arr[i], maxe = maxe, arr[i] if arr[i] > maxe else maxe
    return arr

if __name__ == "__main__":
    print(replaceElements([1,2]))
    print(replaceElements([17,18,5,4,6,1]))