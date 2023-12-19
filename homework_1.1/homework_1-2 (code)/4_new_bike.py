month = 0
counter_money = 0
for i in range(12):
    print("Какую сумму хотим положить?")
    while True:
        print(f"Введите сумму, которую хотите положить в {i+1} месяце: ", end=" ")
        money=input()
        if money.isdigit()==True:
            counter_money+=int(money)
            month+=month
            break
        else:
            print("Вы не ввели сумму числом.")
print("Итого вы накопили:", counter_money)