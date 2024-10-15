Price_string= input('Enter the price ')
Price= int(Price_string)
Discount_string = input ('Enter the discount in % ')
Discount= int(Discount_string)*0.01
Discountedprice = Price - Discount*Price
Reduction = round(Price - Discountedprice,2)
print(f'Product price: {Price}')
print(f' Discount: {Discount_string}%')
print(f'Price with discount: {Discountedprice}')
print(f'Reduction: {Reduction}  ')

