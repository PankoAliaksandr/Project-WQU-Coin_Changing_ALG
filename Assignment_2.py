# Solving function
def BestChange(coins, total_amount):
    if total_amount == 0:
            return []
    for coin in coins:
        if coin <= total_amount:
            return [coin] + BestChange(coins, total_amount - coin)


coins = [25, 10, 5, 1]
amount = eval(raw_input("Enter the total sum to change:"))
print BestChange(coins, amount)
