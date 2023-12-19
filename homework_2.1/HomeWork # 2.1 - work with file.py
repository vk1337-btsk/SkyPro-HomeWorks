import os
import random


def create_file_with_words(file_name_words):
    """
    Функция для создания файла words.txt в текущей папке со словами на английском языке для игры в "угадай слова"
    """
    # Список из 100 слов на английском языке
    words = ['Mother', 'Problem', 'School', 'Number', 'Home', 'Person', 'Question', 'Book', 'Food', 'Question', 'Fact',
             'Room', 'Work', 'Year', 'Idea', 'System', 'Woman', 'Country', 'Table', 'Man', 'Father', 'Example',
             'Country', 'Program', 'World', 'Home', 'Government', 'People', 'Question', 'Father', 'Day', 'Family',
             'Mother', 'School', 'Problem', 'Example', 'Fact', 'Fact', 'State', 'State', 'Company', 'Life', 'Food',
             'Friend', 'Place', 'Case', 'Woman', 'Company', 'Water', 'Child', 'Life', 'Family', 'Fact', 'Area', 'Money',
             'Table', 'Group', 'Job', 'Room', 'Part', 'System', 'Work', 'Fact', 'Money', 'Number', 'Place', 'Hand',
             'Book', 'People', 'Hand', 'Time', 'Government', 'Way', 'Part', 'Group', 'Area', 'Problem', 'Business',
             'Person', 'Water', 'Business', 'Job', 'Government', 'Idea', 'Question', 'Company', 'Question', 'Child',
             'World', 'Case', 'Program']

    random.shuffle(words)

    # Создаём файл words.txt, если его нет в папке и заменяем, если он был
    if os.path.isfile(file_name_words):
        with open(file_name_words, "r+", encoding="utf-8") as file:
            for word in words:
                file.write(f"{word}\n")
    else:
        with open(file_name_words, "x", encoding="utf-8") as file:
            for word in words:
                file.write(f"{word}\n")

    file.close()

    return print("Файл создан, можно начинать играть!")


def write_the_record_to_a_file(user_name, user_point, file_name_history):
    if os.path.isfile(file_name_history):
        with open(file_name_history, "a", encoding="utf-8") as file:
            file.write(f"{user_name.capitalize()} {user_point}\n")
    else:
        with open(file_name_history, "a", encoding="utf-8") as file:
            file.write(f"{user_name.capitalize()} {user_point}\n")

    file.close()

    return


def input_name_user():
    """
    Функция для ввода пользователем своего имени
    """

    print("Привет! Давай знакомиться! ", end="")

    user_name = ""
    while user_name == "":
        user_name = input("Введите ваше имя: ")

    return user_name


def game_guess_the_words(user_name):
    """
    Функция, в которой проходит вся игра в "угадай слова"
    """

    print(f"""\n{user_name.capitalize()}, давай поиграем в игру. Я буду загадывать слова и перемешивать буквы в них, \
    а ты попытаешься их угадать.
    \rУ тебя будет 3 права на ошибку, а после этого игра закончится и я впишу твой рекорд в историю.\n""")

    # Ввожу переменные: жизни юзера, очки, раунд, список загаданных слов, список отгаданных и неотгаданных слов
    user_life = 3
    user_points = 0
    count_word = 0
    my_list_word = []
    my_list_word_guessed_words = []
    my_list_word_unguessed_words = []

    # Начинаем игру
    while 0 < user_life <= 3:

        count_word += 1

        word, encrypted_word = encrypt_the_word(my_list_word)
        my_list_word.append(word)

        print(f"""{user_name.capitalize()}, я загадал слово № {count_word}, это слово - {encrypted_word}.
        \rПопробуй его расшифровать.""")

        user_answer = input("Введи слово, которое я загадал: ").capitalize()

        if user_answer == word:
            print("Ты угадал! Ты получаешь 10 очков!\n")
            user_points += 10
            my_list_word_guessed_words.append(word)
        else:
            user_life -= 1
            if user_life == 0:
                print(f"Неверно! Я загадал слово {word}. У тебя не осталось жизней. Ты набрал {user_points} очков.\n")
                my_list_word_unguessed_words.append(word)
            else:
                print(f"Неверно! Я загадал слово {word}. Ты теряешь жизнь, у тебя осталось {user_life} жизни.\n")
                my_list_word_unguessed_words.append(word)

    print(f"""{user_name.capitalize()}, ты сыграл {count_word} раундов и набрал {user_points} очков.
    \rТы отгадал {len(my_list_word_guessed_words)} слов: {my_list_word_guessed_words}.
    \rТы не отгадал {len(my_list_word_unguessed_words)} слов: {my_list_word_unguessed_words}.\n""")
    return user_points


def encrypt_the_word(my_list_word):
    """
    Функция для случайного выбора слова из файла и его зашифровки
    """
    file = open(file_name_words, "r")

    words = list(map(str.strip, file.readlines()))

    file.close()

    while True:
        word = random.choice(words)
        if word not in my_list_word:
            break

    while True:
        shuffled_word = list(word)
        random.shuffle(shuffled_word)
        encrypted_word = "".join(shuffled_word)
        if encrypted_word != word:
            break

    return word, encrypted_word


def print_statistics(file_name_history):
    """
    Функция, печатающая статистику игр
    """
    with open(file_name_history, "r", encoding="utf-8") as file:
        history = [(el.split()[0], int(el.split()[1])) for el in file.readlines()]

        count_game = len(history)
        max_record = max(history, key=lambda history: history[1])[1]

    text = f"""Всего игр сыграно: {count_game}.
    \rМаксимальный рекорд: {max_record}"""

    return text


# Запуск программы
if __name__ == "__main__":
    # Задаём имена файлам
    file_name_words = "HomeWork # 2.1 - words.txt"
    file_name_history = "HomeWork # 2.1 - history.txt"

    # Создаём или перезаписываем файл "words.txt" со списком слов для игры
    create_file_with_words(file_name_words)

    # Запрашиваем имя у пользователя и возвращаем имя пользователя
    user_name = input_name_user()

    # Проводим игру "угадай слова" и возвращаем количество очков
    user_points = game_guess_the_words(user_name)

    # Создаём или дописываем в файл "history.txt" имя пользователя и набранные очки
    write_the_record_to_a_file(user_name, user_points, file_name_history)

    # Печатаем статистику ранних игр
    print(print_statistics(file_name_history))
