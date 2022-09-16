tickets = int(input('Сколько билетов Вы хотите приобрести? '))
summ = 0
for i in range(tickets):
    age = int(input('Введите возраст посетителя № ' + str(i + 1) + ': '))
    if age < 18:
        print('Вход бесплатный')
    elif 18 <= age <= 25:
        summ += 990
        print('Цена билета - 990 рублей')
    elif age > 25:
        summ += 1390
        print('Цена билета - 1390 рублей')
print('Стоимость билета - ', summ, 'рублей')
if tickets >= 3:
    summ -= summ * 10 / 100
print('Стоимость билета со скидкой - ', summ, 'рублей')
