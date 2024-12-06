price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for product, price in price_list.items():
    print(f"{product} : {price}")

i = 0 
for price in price_list.values():
    i += price
    i = round(i, 2)
print(i)


for product, price in price_list.items():
    new_price = price - 0.1 * price
    new_price = round(new_price, 2)
    print(f" {product} : {new_price}")




total_after = sum(new_price for price in price_list.values() for new_price in [price - 0.1 * price])
print(total_after)    
   
