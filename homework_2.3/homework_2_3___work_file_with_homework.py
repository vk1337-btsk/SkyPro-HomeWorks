from homework_2_3___file_with_class_questions import Questions
from random import shuffle
import json


def open_json_file_and_save(json_file):
    """ Функция получения информации из файла json"""
    with open(json_file, "r") as file:
        data = json.load(file)
    return data


def question_game(question_from_file, i):
    """Функция, в которой реализуется процесс игры для одного цикла"""
    # Создает экземпляр класса Questions, передавая значения атрибутов в качестве аргументов
    question = Questions(*question_from_file.values(), i)

    # Выводим текущий вопрос
    print(question.build_question())

    # Запрашиваем у пользователя ответ на вопрос
    question.user_answer = input("Введите ответ на вопрос: ")
    while question.user_answer is None or question.user_answer == "":
        question.user_answer = input("Пожалуйста, введите ответ на вопрос: ")

    # Меняем статус вопроса с незаданного на заданный
    question.question_asked = True

    # Выводим ответ пользователю в зависимости от правильности ответа
    if question.is_correct():
        # Вычисляем количество баллов за верно отвеченный вопрос
        question.points = question.get_points()
        print(question.build_positive_feedback())
    else:
        print(question.build_negative_feedback())

    return question


def print_statistics(list_questions):
    """Функция, печатающая статистику после игры"""
    sum_correct_answers = sum([1 if obj.points != 0 else 0 for obj in list_questions])
    sum_questions = len(list_questions)
    sum_points = sum([obj.points for obj in list_questions])
    text = f"""
    \rВот и всё!
    \rОтвечено {sum_correct_answers} вопроса из {sum_questions}
    \rНабрано баллов: {sum_points}"""

    return text


if __name__ == "__main__":

    name_json_file = "homework_2_3___file_json.json"

    # Получаем список вопросов из файла, создаём свой для дальнейшей работы и перемешиваем его
    list_questions_from_the_file = open_json_file_and_save(name_json_file)
    shuffle(list_questions_from_the_file)

    # С помощью генератора списков заполняем наш список вопросов (и внутри цикла обрабатываем вопрос)
    my_list_questions = [question_game(q, i) for i, q in enumerate(list_questions_from_the_file, 1)]

    print(print_statistics(my_list_questions))
