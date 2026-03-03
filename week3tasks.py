def calculate_discounted_price(price, discount_percent):
    discount=price/100*discount_percent

    return price-discount



print(calculate_discounted_price(150,35))


