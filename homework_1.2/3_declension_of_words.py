def python_word():
    print("Давай посклоняем слова.")
    while True:
        python=input("Сколько питонов у тебя есть? ")
        if python.isdigit()==True and int(python)>=0:
            python=int(python)
            if python==0 or python%10==0:
                python_word="питонов"
            elif 11<=python<=14 or 11<=python%100<=14 or 5<=python%10<=9:
                python_word="питонов"
            elif 2<=python%10<=4:
                python_word="питона"
            else:
                python_word="питон"
            break
        else:
            print("Прости, но тебе нужно ввести число.")
        break
    print(f"Я тебя понял, у тебя есть {python} {python_word}")

if __name__=="__main__":
    python_word()