while True:
    money_usd = input("Введите сумму в долларах: ")
    if money_usd.isdigit()==True:
        money_rub = int(money_usd) * 70.38
        money_eur = money_rub / 100
        print(int(money_eur))
    else:
        print("Вы не ввели число.")