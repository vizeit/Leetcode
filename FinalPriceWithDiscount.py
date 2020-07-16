def finalPrices(prices):
    if len(prices) < 2: return prices
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] <= prices[i]:
                prices[i] -= prices[j]
                break
    return prices
if __name__ == "__main__":
    print(finalPrices([8,4,6,2,3])) 
    print(finalPrices([1,2,3,4,5]))
    print(finalPrices([10,1,1,6]))
        