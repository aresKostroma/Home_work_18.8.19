a = int(input('Сколько билетов вы хотите приобрести? '))
b = (0)
for i in range(a):
    age = int(input('введите возраст: '))
    if age < 18:
        b = b + 0
    elif 18 < age < 25:
        b = b + 990
    else:
        b = b + 1390
print('Сумма к оплате: ', (int(b * 0.9 if a > 3 else b)))

