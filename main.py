tickets = int(input('Сколько билетов Вы хотите приобрести? '))
age = int(input('Сколько Вам лет? '))
price = 0

if age < 18:
    print('Вход бесплатный')
elif 18 <= age <= 25:
    price = 990
    print('Цена билета - 990 рублей')
elif age > 25:
    price = 1390
    print('Цена билета - 1390 рублей')

price *= tickets
if tickets >= 3:
    price -= price * 10 / 100
print('Стоимость билета - ', price, 'рублей')
