#!/usr/bin/python3

""" Contains makeChange function"""

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the value at total is still infinite, it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
