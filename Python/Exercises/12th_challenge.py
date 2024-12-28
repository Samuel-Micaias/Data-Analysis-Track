price    = float(input('Enter product price: '))
discount = float(input('Discount percentage: '))
discount_price = price - ((price * discount) / 100)
print('The product costs R${:.2f100}, I will give a discount of {}%, and with the discount, the product costs R${:.2f}'.format(price, discount, discount_price))
