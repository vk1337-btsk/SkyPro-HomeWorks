def english_lesson():
    print("Привет! Предлагаю проверить свои знания английского!")
    print('Набери "ready", чтобы начать! Или "not ready", если не готов')
    while True:
        status=input()
        if status=="ready":
            s1=["My name ___ Vova", "I ___ a coder","I live ___ Moscow"]
            s2=["is", "am", "in"]
            correct_answer=0
            for i in range(len(s1)):
                print("Впишите пропущенное слово в предложение: ", s1[i])
                answer=input()
                if answer==s2[i]:
                    correct_answer+=1
                    print("Ответ верный!")
                else:
                    print("Неправильно. Правильный ответ", s2[i])
            print("Вот и всё, вы ответили на", correct_answer, "вопросов из", len(s1), "верно, это", int(correct_answer/len(s1)*100), "процентов")

        elif status=="not ready":
            print("До следующего раза. Пока!")
            break
        else:
            print('Набери "ready", чтобы начать!')
            continue

if __name__=="__main__":
    english_lesson()