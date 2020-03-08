def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        print_white_discount = price
    else:
        print_white_discount = price - price * discount / 100
    return(print_white_discount)

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 5000.0, 'discount': 50}

product['with discount'] = discounted(product['price'], product['discount'])

print(product)