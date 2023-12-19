def english_lesson():
    # Определение переменных
    questions = ["My name ___ Vova.", "I ___ a coder.", "I live ___ Moscow.", "How ___ you?"]
    correct_answers = ["is", "am", "in", "are"]
    count_try = ["попыток", "попытка", "попытки"]
    count_correct_answers = 0
    count_score = 0
    
    # Начало программы, ввод имени пользователя
    print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
    if input("Введите'ready', если готовы: ").lower() != "ready":
      print("Кажется, вы не хотите играть. Очень жаль.")
    else:
        user_name = input("Напишите, как вас зовут: ").capitalize()
        print(f"Привет, {user_name}, давай начнем тренировку!")

        # Проверка знания английского (цикл по спискам с вопросами и ответами)
        for i in range(len(questions)):
            print(f"\n{user_name}, впишите в предложение № {i+1} пропущенное слово: \n{questions[i]}")

            # Начинаем цикл с 3-мя попытками для ввода
            for j in range(3, 0, -1):

                # Ввод слова пользователем и проверка на корректность ввода (отсутствие чисел)
                while True:
                    user_answer = input("Впишите пропущенное слово: ").lower()          
                    if user_answer.isalpha() == False:    
                        print("Введите корректный вариант ответа (только текст).")
                    else:
                        break        
                            
                # Результат ответа пользователя
                if user_answer == correct_answers[i]:
                    count_correct_answers += 1
                    count_score += j * 10
                    print(f"Ответ верный! Вы получаете {j * 10} баллов!")
                    break
                else:
                    print(f"Неправильно. У вас осталось {j - 1} {count_try[j-1]}.")     

        # Подсчет верных ответов (в процентах)
        count_correct_answers_in_percent = round(count_correct_answers / len(questions) * 100, 2)

        # Вывод итогов тестирования
        print(f"\nВот и всё, {user_name}! \nВы ответили на {count_correct_answers} вопросов из {len(questions)} верно.\n")
        print(f"Вы заработали {count_score} баллов. \nЭто {count_correct_answers_in_percent} процентов.")

# Запуск программы
if __name__ == "__main__":
    english_lesson()
