def apply_discount(prices, discount):
    return [price - (price * discount / 100) for price in prices]


prices = [100, 250, 400, 50]

discounted_prices = apply_discount(prices, 10)  
print(discounted_prices)
