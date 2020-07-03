from collections import Counter
def numJewelsInStones(J: str, S: str) -> int:
    return sum(Counter(S)[i] for i in J)

if __name__ == "__main__":
    print(numJewelsInStones('z', 'ZZ'))