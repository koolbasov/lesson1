# stock = [
#     {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1,
#        'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
#     {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#     {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
# ]
#
# print(type(stock))
# print(type(stock[0]))
# print(type(stock[0]['recomended']))

weather_cast = {"city": "Москва", "temperature": "20"}
print(weather_cast['city'])
weather_cast["temperature"] = int(weather_cast['temperature']) - 5
print(weather_cast)
print('country' in weather_cast)
print(weather_cast.get('country', 'Россия'))
weather_cast['date'] = "27.05.2019"
print(weather_cast)
print(len(weather_cast))