# Use dynamic programming to fill in the next ten values of MinNumCoins(m) (i.e., for 13 ≤ m ≤ 22).


def dp_change(money, coins):
    MinNumCoins = {}
    MinNumCoins[0] = 0
    for m in range(1, money+1):
        MinNumCoins[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                if MinNumCoins[m-coins[i]]+1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m-coins[i]]+1
    return MinNumCoins


MinNumCoins = dp_change(22, [1, 4, 5])

output = ' '.join([str(v) for k, v in MinNumCoins.items() if k >= 13])
print(output)
