from collections import defaultdict
def canBeEqual(target, arr):
    d = defaultdict(int)
    for i, j in zip(target, arr):
        d[i]+=1
        if i in d and d[i] == 2: del d[i]
        d[j]+=1 
        if j in d and d[j] == 2: del d[j]
    return False if len(d) else True

if __name__ == "__main__":
    print(canBeEqual([1,2,3,4], [2,4,1,3]))
    print(canBeEqual([7], [7]))
    print(canBeEqual([1,12], [12,1]))
    print(canBeEqual([3,7,9], [3,7,11]))
    print(canBeEqual([1,1,1,1], [1,1,1,1]))
    print(canBeEqual([234,268,148,639,341,689,178,918,646,768,24,306,374,57,155,936,22,588,980,556,476,548,312,596,991,609,288,869,763,679,925,180,562,180,546,517,436,690,377,570,766,239,882,74], [288,155,306,24,925,679,22,588,936,517,312,639,476,689,882,548,690,556,570,74,980,991,377,148,546,768,763,646,869,57,178,436,374,180,239,562,180,234,268,596,918,609,341,766]))

    

