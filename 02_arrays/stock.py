def max_profit_brute(prices):
    best = 0

    for buy in range(len(prices)):
        for sell in range(buy+1,len(prices)):
            profit = prices[sell] - prices[buy]
            best = max(profit,best)

    return best 

def max_profit(prices):

    min_price = float('inf')
    best = 0 

    for price in prices:

        min_price = min (min_price, price)
        best = max(best , price - min_price)

    return best

def max_profit_ii(prices):

    profit = 0

    for i in range(1,len(prices)):

        if prices[i]> prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit 