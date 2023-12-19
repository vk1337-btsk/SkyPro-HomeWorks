def english_lesson():
    # Определение переменных
    questions = ["My name ___ Vova.", "I ___ a coder.", "I live ___ Moscow."]
    correct_answers = ["is", "am", "in"]
    count_correct_answers = 0
    count_score = 0

    # Начало программы, ввод имени пользователя
    print("Привет! Предлагаю проверить свои знания английского! \nНапишите, как вас зовут.")
    user_name = input().capitalize()
    print(f"Привет, {user_name}, давайте начнем тренировку!")

    # Проверка знания английского (цикл по словарям с вопросами и ответами)
    for i in range(len(questions)):
        print(f"\n{user_name}, впишите в предложение № {i+1} пропущенное слово: \n{questions[i]}")

        # Проверка слова пользователя на отсутствие чисел
        while True:
            user_answer = input().lower()
            if user_answer.isalpha():
                break

        # Результат ответа пользователя        
        if user_answer == correct_answers[i]:
            count_correct_answers += 1
            count_score += 10
            print("Ответ верный! Вы получаете 10 баллов!")
        else:
            print(f"Неправильно. Правильный ответ: {correct_answers[i]}")

    # Подсчет верных ответов (в процентах)
    count_correct_answers_in_percent = round(count_correct_answers / len(questions) * 100, 2)

    # Вывод итогов тестирования
    print(f"\nВот и всё, {user_name}! \nВы ответили на {count_correct_answers} вопросов из {len(questions)} верно.\n")
    print(f"Вы заработали {count_score} баллов. \nЭто {count_correct_answers_in_percent} процентов.")

# Запуск программы
if __name__ == "__main__":
    english_lesson()
