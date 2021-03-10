# Dynamic Program Change Problem -
# Input: An integer money and an array coins = (coin1, ..., coind).
# Output: The minimum number of coins with denominations coins that changes money.


def dp_change(money, coins):
    MinNumCoins = {}
    MinNumCoins[0] = 0
    for m in range(1, money+1):
        MinNumCoins[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                if MinNumCoins[m-coins[i]]+1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m-coins[i]]+1
    return MinNumCoins[money]


print(dp_change(22, [1, 4, 5]))
