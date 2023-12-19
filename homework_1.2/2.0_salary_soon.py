def zarplata():
    print("Привет! Давай узнаем, когда у тебя зарплата!")
    while True:
        day=input("Введите сегодняшнее число: ")
        if day.isdigit()==True:
            day=int(day)
            if day==5 or day==20:
                print(f"Зарплата уже сегодня! {day} числа")
            elif 0<=day<5:
                print("Ближайшая зарплата 5-го числа, через", 5-day, "д.")
            elif 5<day<20:
                print("Ближайшая зарплата 20-го числа, через", 20-day, "д.")
            elif 20<day<=30:
                print("Ближайшая зарплата 5-го числа, через", 30-day+5, "д.")
            else:
                print("Введите настоящее число месяца. В месяце 30 дней.")
                continue
            if input("Желаете продолжить? (да / нет) ")=="да":
                continue
            else:
                break
        else:
            print("Введите число.")

if __name__=="__main__":
    zarplata()