def kidsWithCandies(candies, extraCandies):
    m = max(candies)
    return [True if candy+extraCandies >= m else False for candy in candies]

if __name__ == "__main__":
    print(kidsWithCandies([12,1,12], 10))