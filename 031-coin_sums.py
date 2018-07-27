from functools import lru_cache

@lru_cache()
def change_recursive(change, valid_coins):
    """
    Calculate amount of ways to get to the value change by summing the values in valid_coins.
    Order is not disregarded, (2, 1) is the same as (1, 2), counting as one possible combination
    :param change:
    :type change: int
    :param valid_coins: List of valid coin denominations in ascending order
    :type valid_coins: [int]
    :return: Amount of possible combinations
    :rtype: int
    """
    valid = tuple(c for c in valid_coins if c <= change)
    if len(valid) <= 1 or change <= 1:
        return 1
    return change_recursive(change, valid[:-1]) + change_recursive(change-valid[-1], valid)

def change_iterative(change, valid_coins):
    """
    Calculate amount of ways to get to the value change by summing the values in valid_coins.
    Order is not disregarded, (2, 1) is the same as (1, 2), counting as one possible combination
    :param change:
    :type change: int
    :param valid_coins: List of valid coin denominations in ascending order
    :type valid_coins: [int]
    :return: Amount of possible combinations
    :rtype: int
    """
    # will contain the change sum as key (with increasing values from 0...change) with the list of possibilities as a
    # value. The list of possibilities contains the amount of possible combinations to create a sum of t using only the
    # coin with value <= i
    result_table = {}
    # to create a sum of target 0 with any coins, there is one possible combination (which is using no coins)
    result_table[0] = [1] * len(valid_coins)
    # to create a sum of target 1 there is only one possibility, using one coin of value 1
    result_table[1] = [1] * len(valid_coins)
    # calculates the possibilities to reach a sum of value t with progressively more coins
    for t in range(2, change+1):
        required_coins = [1] * len(valid_coins)
        for i, coin in enumerate(valid_coins):
            # using only coins of value <= 1 there is only one option to create N: N*1
            if coin == 1: continue
            # coins that are greater than the target sum dont add a possibility, since adding one of them would
            # increase the sum above the target value
            if coin > t: required_coins[i] = required_coins[i - 1]; continue
            # the amount of possibilities to create a sum t with coins <= coin in value is given by the amount of
            # possibilities to create the same sum without the largest coin plus the amount of possibilities to create
            # the value sum-value_of_largest_coin
            required_coins[i] = required_coins[i - 1] + result_table[t - coin][i]
        result_table[t] = required_coins
    return result_table[change][-1]

if __name__ == '__main__':
    coins = (1, 2, 5, 10, 20, 50, 100, 200)     # value in pence
    print(change_iterative(200, coins))
    print(change_recursive(200, coins))

    """
    python3 -m timeit -s "from 031-coin_sums import change_iterative, change_recursive; coins = [1, 2, 5, 10, 20, 50, 100, 200]; val= 200" "change_iterative(val, coins)"
    1000 loops, best of 3: 280 usec per loop
    """
    """
    python3 -m timeit -s "from 031-coin_sums import change_iterative, change_recursive; coins = (1, 2, 5, 10, 20, 50, 100, 200); val= 200" "change_recursive(val, coins)"
    10000000 loops, best of 3: 0.0946 usec per loop
    """
