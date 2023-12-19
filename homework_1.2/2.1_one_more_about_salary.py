def zarplata_and_bonus():    
    print("Давайте посчитаем то, что вы заработали")
    while True:
        zarplata=input("Введите вашу зарплату: ")
        if zarplata.isdigit():
            zarplata=int(zarplata)
            print("Отлично, а теперь давай посчитаем бонус.")
            break
        else:
            print("Введите вашу зарплату (числом).")

    print("Ваш план на квартал был - 1000 книг. \n Сколько вы продали?")
    while True:
        sale=input("Введите количество книг, сколько вы продали: ")
        if sale.isdigit():
            sale=int(sale)
            if sale<1000:
                bonus=0
            elif 1000<=sale<1500:
                bonus=int(zarplata*0.1)
                bonus_percent="10 %"
            elif 1500<=sale<2000:
                bonus=int(zarplata*0.15)
                bonus_percent="15 %"
            elif sale>=2000:
                bonus=(zarplata*0.2)
                bonus_percent="20 %"
            break       
    if bonus==0:
        print(f"Размер вашего бонуса {bonus} рублей. К сожалению, вы не выполнили план.")
    else:
            print(f"Отлично, вы заработали бонус в размере {bonus} рублей. Это {bonus_percent} от вашей зарплаты {zarplata} рублей.")

if __name__=="__main__":
    zarplata_and_bonus()