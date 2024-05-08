list_car = ["BMW", "MB", "LADA", "KIA", "HONDA"]

for i in list_car:
    print('Я езжу на автомабиле марки', (i))

cars_count = 0
for i in range(len(list_car)):
    print(f'Я езжу на автомабиле марки {list_car[i]}')
    cars_count += 10

print(cars_count)


