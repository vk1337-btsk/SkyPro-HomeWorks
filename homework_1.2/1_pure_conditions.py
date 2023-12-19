def stirka():
    print("Добро пожаловать в стиральную машинку!")
    print("В каком режиме вы желаете постирать?")
    while True:
        regime=input("Введите режим (обычный / экспресс / хлопок): ")
        if regime=="обычный":
            time=90
            break
        elif regime=="экспресс":
            time=20
            break
        elif regime=="хлопок":
            time=120
            break
        else:
            print("Простите, я не знаю такого режима.")

    while True:
        push_ups=input("Желаете включить отжим? (да / нет): ")
        if push_ups=="да":
            time+=10
            break
        elif push_ups=="нет":
            time-=10
            break
        else:
            print("Ответьте, пожалуйста, да или нет.")

    while True:
        rinsing=input("Желаете включить дополнительное полоскание? (да / нет): ")
        if rinsing=="да":
            time+=10
            break
        elif rinsing=="нет":
            time-=10
            break
        else:
            print("Ответьте, пожалуйста, да или нет.")

    print(f"Отлично! Время стирки займёт {time} минут")

if __name__=="__main__":
    stirka()