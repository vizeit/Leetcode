from collections import Counter

def uniqueOccurrences(arr):
    d = Counter(arr)
    return len(d.keys()) == len(set(d.values()))


if __name__ == "__main__":
    print(uniqueOccurrences([1,2,2,1,1,3]))
    print(uniqueOccurrences([1,2]))
    print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))