# Задание 2
def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

product_price = format_price(56.24)
print(product_price)

# Задание 1
# def get_summ(one, two, delimeter='&'):
#     result = f'{str(one)} {delimeter} {str(two)}'
#     return result.upper()
#
# print(get_summ('learn', 'python'))
# print(get_summ(5, 10))

# def discounted(price, discount, max_discount=20):
#     price = abs(price)
#     discount = abs(discount)
#     max_discount = abs(max_discount)
#     if max_discount >= 100:
#         raise ValueError('Максимальная скидка не должна быть больше 100%')
#     if discount >= max_discount:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     return price_with_discount
#
#
# print(discounted(100, 5))
# print(discounted(100, 50))
# print(discounted(100, 50, max_discount=60))
