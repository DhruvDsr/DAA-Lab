def max_profit(prices, fee):
    if not prices:
        return 0
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    return cash

print(max_profit([1, 3, 2, 8, 4, 9], 2))