ticket = int(input("Количество билетов, которые нужно приобрести: "))
print(ticket)
sum = 0 #инициализация суммы
for i in range(ticket):
    print("Сколько вам лет?")
    age = int(input())
    if age < 18:
         price = int(0)                #бесплатно
    if 18 <= age and age <= 25:
         price = int(990)
    if age > 25:
        price = int(1390)
    sum = sum + price                  # вычисление суммы
print(sum)                             #вывод суммы
if ticket > 3:
    sum = sum - sum*0.1
    print("Сумма к оплате со скидкой 10%:", sum)