import os
import json


def create_json_file_with_students(file_name_students):
    """
    Функция, которая создаёт файл json с данными по студентам
    """
    data = [
        {
            "pk": 1,
            "full_name": "Jane Snake",
            "skills": ["Python", "Go", "Linux"]
        },
        {
            "pk": 2,
            "full_name": "Sheri Torres",
            "skills": ["Java", "Swift", "Fortran", "Basic"]
        },
        {
            "pk": 3,
            "full_name": "Burt Stein",
            "skills": ["Planning", "Negotiation", "Management", "Sales"]
        },
        {
            "pk": 4,
            "full_name": "Bauer Adkins",
            "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
        }
    ]

    # Сериализация в JSON и сохранение в файл
    with open(file_name_students, "w") as json_file:
        json.dump(data, json_file)

    return


def create_json_file_with_professions(file_name_professions):
    """
    Функция, которая создаёт файл json с данными по профессиям
    """
    data = [
        {
                "pk": 1,
                "title": "Backend",
                "skills": ["Python", "Linux", "Docker", "SQL", "Flask"]
        },
        {
                "pk": 2,
                "title": "Frontend",
                "skills": ["HTML", "CSS", "React", "JavaScript"]
        },
        {
                "pk": 3,
                "title": "Testing",
                "skills": ["Windows", "MacOS", "SQL", "Jira"]
        }
    ]
    # Сериализация в JSON и сохранение в файл
    with open(file_name_professions, "w") as json_file:
        json.dump(data, json_file)

    return


def check_file_or_create_files(file_name_students, file_name_professions):
    """
    Функция для удобства. Если файлы "students.json" и "professions.json" есть - используем их. В ином случае - создаём
    """
    # Для удобства и простоты: если файлы с именами как в ДЗ уже есть, то мы работаем с ними, если нет, то создаём свои
    if not (os.path.isfile(file_name_students) and os.path.isfile(file_name_professions)):
        create_json_file_with_students(file_name_students)
        create_json_file_with_professions(file_name_professions)
        print(f"Мы создали файлы {file_name_students} и {file_name_professions}, т.к. они отсутствовали.")
    else:
        print("Файлы уже есть, поэтому будем использовать их.")

    return


def get_information_about_the_student(file_name_students, num_student):
    """
    Функция получения информации о студенте из файла json и возвращении
    """
    # Открываем файл json и выгружаем данные из него
    with open(file_name_students, "r") as file:
        data = json.load(file)

    # Проходим по информации, если такой специальности нет - выводим строку с информацией о её отсутствии,
    # в случае наличия - словарь с информацией
    data_student1 = "У нас нет такого студента."
    for i in range(len(data)):
        if data[i]["pk"] == num_student:
            data_student1 = data[i]
            break

    return data_student1


def print_information_about_the_student(info_student):
    text = f"""
    \rСтудент: {info_student["full_name"]}
    \rЗнает: {", ".join(info_student["skills"])}\
    """
    return text


def get_information_about_the_professions(file_name_professions, students_professions1):
    """
    Функция получения информации о специальности
    """
    # Открываем файл json и выгружаем данные из него
    with open(file_name_professions, "r") as file:
        data = json.load(file)

    # Проходим по информации, если такого студента нет - выводим строку с информацией о его отсутствии,
    # в случае наличия - словарь с информацией
    data_profession1 = "Нет такой специальности"
    for i in range(len(data)):
        if data[i]["title"] == students_professions1:
            data_profession1 = data[i]
            break

    return data_profession1


def print_information_about_the_professions(info_profession, info_student):
    # Определяем скиллы, которые студент знает
    student_knows_skills = list(set(info_profession["skills"]) & set(info_student["skills"]))
    if len(student_knows_skills) == 0:
        text_student_knows_skills = f'Студент {info_student["full_name"]} не имеет необходимых знаний'
    else:
        text_student_knows_skills = f'Студент {info_student["full_name"]} знает: {", ".join(student_knows_skills)}'

    # Определяем скиллы, которые студент не знает
    student_dont_knows_skills = set(info_profession["skills"]) - set(info_student["skills"])
    if len(student_dont_knows_skills) == 0:
        text_student_dont_knows_skills = f'Студент {info_student["full_name"]} ______'
    else:
        text_student_dont_knows_skills = f'Студент {info_student["full_name"]} не знает: {", ".join(student_dont_knows_skills)}'

    # Определяем пригодность студента
    student_suitability = int(len(student_knows_skills) / len(info_profession["skills"]) * 100)
    text = f"""
    \rПригодность: {student_suitability} %
    \r{text_student_knows_skills}
    \r{text_student_dont_knows_skills}
    """
    return text


def input_number_student():
    """
    Функция для ввода номера студента
    """
    number_student1 = input("Введите номер студента (число): ")
    while not number_student1.isdigit():
        number_student1 = input("Пожалуйста, введите номер студента (числом): ")
    number_student1 = int(number_student1)

    return number_student1


def input_professions_students():
    students_professions1 = input("Введите специальность студента: ")
    while students_professions1 == "":
        students_professions1 = input("Пожалуйста, введите специальность студента: ")

    return students_professions1


if __name__ == "__main__":
    # Присваиваем названия переменным - файлам формата json c данными по студентам и профессиям
    file_students = "HomeWork # 2.2 - students.json"
    file_professions = "HomeWork # 2.2 - professions.json"

    # Проверяем наличие нужных файлов. В случае их отсутствия - создаём их
    check_file_or_create_files(file_students, file_professions)

    # Вводим номер студента для дальнейшего поиска информации о нём
    number_student = input_number_student()

    # Получаем данные о студенте из файла json
    data_student = get_information_about_the_student(file_students, number_student)

    # Если такого студента нет - выводим сообщение об отсутствии, если такой студент есть - выводим информацию о нём
    if isinstance(data_student, str):
        print(data_student)
    else:
        print(print_information_about_the_student(data_student))

        # Вводим специальность для определения пригодности студента
        students_professions = input_professions_students()

        # Получаем данные о специальности из файла json
        data_profession = get_information_about_the_professions(file_professions, students_professions)

        # Если такой специальности нет - выводим сообщение об отсутствии, если есть - выводим информацию о ней
        if isinstance(data_profession, str):
            print(data_profession)
        else:
            print(print_information_about_the_professions(data_profession, data_student))
