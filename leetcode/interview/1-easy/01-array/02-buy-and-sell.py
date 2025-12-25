prices = [7,1,5,3,6,4]

diffs = [prices[i] - prices[i-1] for i in range(1, len(prices))]

print(diffs)

profit = sum([x for x in diffs if x>0])
print(profit)
