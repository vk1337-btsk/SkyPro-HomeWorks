def create_dictionary(difficulty_level):
    """
    Эта функция для выбора словаря со словами для игры, она принимает введённый пользователем уровень сложности и возвращает нужный словарь
    """
    
    # Словарь лёгкий    
    words_easy = { 
        "family":"семья", 
        "hand": "рука", 
        "people":"люди", 
        "evening": "вечер",
        "minute":"минута", 
    }

    # Словарь средний
    words_medium = { 
        "believe":"верить", 
        "feel": "чувствовать", 
        "make":"делать", 
        "open": "открывать",
        "think":"думать", 
    }

    # Словарь сложный
    words_hard = { 
        "rural":"деревенский", 
        "fortune": "удача", 
        "exercise":"упражнение", 
        "suggest": "предлагать",
        "except":"кроме", 
    }
    
    dictionary_difficulty_level = {"легкий" : words_easy, "лёгкий" : words_easy, "средний" : words_medium, "сложный" : words_hard}
    words = dictionary_difficulty_level.get(difficulty_level)
    
    return words


def determine_user_level_and_print_statistics(answers):
    """
    Эта функция для определения ранга пользователя и печати статистики игры.
    Она принимает введённый пользователем словарь ответов и возвращает уровень пользователя и статистику.
    """
    # Словарь ранга пользователя
    levels = {
        0: "Нулевой", 
        1: "Так себе", 
        2: "Можно лучше", 
        3: "Норм", 
        4: "Хорошо", 
        5: "Отлично",
    }       
    
    # Создаём списки с правильными и неправильными ответами
    correct_answers = []
    incorrect_answers = []
    
    # Заполняем списки с правильными и неправильными ответами
    for key, value in answers.items():
        if value == True:
            correct_answers.append(key)
        else:
            incorrect_answers.append(key)

    # Определяем форму вывода для правильных ответов
    if len(correct_answers) == 0:
        print_correct_answers = ["Правильные ответы:", "Отсутствуют"]
    else:
        print_correct_answers = ["Правильные ответы:"]
        print_correct_answers.extend(correct_answers)
    
    # Определяем форму вывода для неправильных ответов
    if len(incorrect_answers) == 0:
        print_incorrect_answers = ["Неправильные ответы:", "Отсутствуют"]
    else:
        print_incorrect_answers = ["Неправильные ответы:"]
        print_incorrect_answers.extend(incorrect_answers)

    # Определяем форму вывода ранга пользователя
    print_level_user = ["Ваш ранг:", levels.get(len(correct_answers)) ]
      
    return print_correct_answers, print_incorrect_answers, print_level_user


"""
Эта программа создана для проверки знаний английского языка у пользователя.
В зависимости от уровня сложности, выбранного пользователем она выписывает слова на английском языке и просит пользователя их перевести.
"""    
if __name__ == "__main__":
    # Создаём словарь для фиксации правильных и неправильных ответов
    answers = {}
    
    # Начало программы, объяснение правил и знакомство с пользователем
    print("Привет! Это программа для проверки твоих знаний английского языка.")
    print("В зависимости от уровня сложности тебе будут предложены разные слова, перевод которых ты должен будешь написать.")
    user_name = input("Давай для начала познакомимся, как тебя зовут? ").capitalize()
    
    print(f"{user_name}, приятно познакомиться!\n")

    # Цикл для ввода пользователем уровня сложности
    while True:
        difficulty_level = input("Какой уровень сложности ты выберешь (лёгкий, средний, сложный)? ")

        if difficulty_level.lower() not in ("лёгкий", "легкий", "средний", "сложный"):
            print("Прости, я не понял какой уровень сложности ты хочешь выбрать... Напиши лёгкий, средний или сложный.")
        else:
            print(f"Я тебя понял, ты выбрал {difficulty_level} уровень сложности. Стартуем!")
            break
        
    words = create_dictionary(difficulty_level)
    
    # Цикл для проверки знаний пользователя английского языка
    for key, value in words.items():
        word_in_english = key
        word_in_russian = value
        
        print(f"\nДавай переведём слово {word_in_english} на русский. В нём {len(word_in_russian)} букв. Начинается на букву {word_in_russian[0]}...")
    
        # Ввод пользователем слова
        answer_user = input("Введите перевод слова: ").lower()
        
        # Проверка слова пользователя с загаданным, вывод промежуточных результатов, а также запись ответа
        if answer_user == word_in_russian:
            print(f"Верно, {word_in_english.capitalize()} — это {word_in_russian}.")
            answers[word_in_english] = answer_user == word_in_russian
        else:
            print(f"Неверно, {word_in_english.capitalize()} — это {word_in_russian}.")
            answers[word_in_english] = answer_user == word_in_russian
    
    # Блок с выводом статистики правильных и неправильных ответов
    print_correct_answers, print_incorrect_answers, print_level_user = determine_user_level_and_print_statistics(answers)
    print()
    print(*print_correct_answers, sep = "\n", end="\n\n")
    print(*print_incorrect_answers, sep = "\n", end="\n\n")
    print(*print_level_user, sep = "\n")