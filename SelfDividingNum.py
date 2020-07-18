def selfDividingNumbers(left, right):
        return [i for i in range(left, right+1) if all(False if j==0 or i % j else True for j in map(int,ascii(i)))]

if __name__ == "__main__":
    print(selfDividingNumbers(1,100))
    print(selfDividingNumbers(200,1000))
    print(selfDividingNumbers(1,10000))

