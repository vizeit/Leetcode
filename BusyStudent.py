def busyStudent(startTime, endTime, queryTime):
    return sum(1 for i, j in zip(startTime,endTime) if queryTime >=i and queryTime <= j)

if __name__ == "__main__":
    print(busyStudent([1,2,3], [3,2,7], 4))
    print(busyStudent([4], [4], 4))
    print(busyStudent([4], [4], 5))
    print(busyStudent([1,1,1,1], [1,3,2,4], 7))
    print(busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5))