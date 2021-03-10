def recursive_change(money, coins):
    """

    Args:
        money ([int]): [total amount of money]
        coins ([ints]): [denominations of currency]

    Returns:
        [list]: [returns the minimum amount of coins required to obtain the value of money]
    """

    flag = None  # start with no coin
    for c in coins:  # iterate through denominations
        if c == money:
            return c  # if denomination matches money, return it
        if c < money:
            flag = c  # flag the denomination
    temp_money = money - flag  # store the remaining balance
    return [flag] + [recursive_change(temp_money, coins)]


money = 76
coins = (5, 4, 1)

print(recursive_change(money, coins))
# Output is greedy, hence it runs through the coins list in the presented order and ends at 1 at the end
# of the first loop so that 1 gets flagged and passed recursively until the remaining balance = 5.
