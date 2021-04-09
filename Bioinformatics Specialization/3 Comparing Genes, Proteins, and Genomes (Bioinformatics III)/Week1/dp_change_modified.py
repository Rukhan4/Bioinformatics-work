# dp_change modified with the following conditions:


# Modify the dp_change algorithm so that the array size required does not
# exceed the value of the largest coin denomination.

# Modify dp_change so that it not only computes the minimum number of coins but also returns these coins.

from collections import OrderedDict


def dp_change(money, coins):
    change = money % coins[0]
    coin_count = []
    max_coin = max(coins)
    cache = OrderedDict({0: 0})

    for m in range(1, money+1):
        coin_count = [[x for x in range(len(coins))] for y in range(change + 1)]
        cache[m] = min(cache[m-c]+1 for c in coins if c <= m)
        while len(cache) > max_coin:
            cache.popitem(False)

    return cache[money], coin_count[0]


print(dp_change(40, [50, 25, 20, 10, 5, 1]))
