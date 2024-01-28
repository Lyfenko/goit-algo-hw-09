def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    result = {coin: 0 for coin in coins}

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                result[i] = coin

    # Заміна наступного рядка
    final_result = {}
    current_amount = amount
    while current_amount > 0:
        coin_used = result[current_amount]
        final_result[coin_used] = final_result.get(coin_used, 0) + 1
        current_amount -= coin_used

    return final_result

