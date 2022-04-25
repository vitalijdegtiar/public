Tickets = int(input( "Введите количество билетов\n"))
Sum = 0
for i in range(1,Tickets+1):
    Age = int(input("Введите возраст поситителя\n"))
    if Age < 18:
     Sum += 0
    elif 18 <= Age <= 25:
     Sum += 990
    elif 25 < Age:
     Sum += 1390

if Tickets > 3:
    print("Вы зарегистрировали более 3-х человек, получите дополнительную скидку 10%!\n")
    print("Сумма покупки со скидкой:\n", int(Sum*0.9), "руб.")
else:
    print("Сумма покупки:\n", Sum, "руб.")