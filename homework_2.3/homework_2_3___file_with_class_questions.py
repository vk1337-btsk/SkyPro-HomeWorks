class Questions:
    """ Класс, позволяющий работать с вопросами \n"""

    def __init__(self, text_question: str, complexity: str, correct_answer: str, number: int):
        """ Конструктор класса.
        \r Обязательные аргументы: текст вопроса, сложность вопроса, верный вариант ответа.
        \r Не обязательные (заданные по умолчанию): задан ли вопрос (по умолчанию False), ответ пользователя
        \r (по умолчанию None), баллы за вопрос (вычисляется в момент инициализации) \n"""

        self.text_questions = text_question
        self.complexity = int(complexity)
        self.correct_answer = correct_answer
        self.question_asked = False
        self.user_answer = None
        self.points = 0
        self.number = number

    def __repr__(self):
        """ Представление объекта в виде строки (для отладки) \n"""
        return f""" Questions:
        \r Вопрос: {self.text_questions};
        \r Правильный ответ: {self.correct_answer};
        \r Сложность вопроса: {self.complexity};
        \r Статус вопроса задан/на задан (False по умолчанию): {self.question_asked};
        \r Ответ пользователя (None по умолчанию): {self.user_answer};
        \r Количество баллов (0 по умолчанию): {self.points}.\n
        """

    def __str__(self):
        """ Представление объекта в виде строки (для пользователя) \n"""
        return f"Вопрос: {self.text_questions}\n"

    def get_points(self):
        """ Возвращает int, количество баллов. Баллы зависят от сложности: за 1 - 10 баллов, за 5 - 50 баллов. \n"""
        self.points = self.complexity * 10
        return self.points

    def is_correct(self):
        """ Возвращает True, если ответ пользователя совпадает с верным ответом, иначе False. \n"""
        return self.user_answer == self.correct_answer

    def build_question(self):
        """ Возвращает вопрос в понятном пользователю виде, например:
        \r Вопрос: What do people often call American flag?
        \r Сложность 4/5 \n"""
        return f"""Вопрос №{self.number}: {self.text_questions}
                \rСложность: {self.complexity}/5"""

    def build_positive_feedback(self):
        """ Возвращает:
        \r Ответ верный, получено __ баллов \n"""
        return f"""Ответ верный, получено {self.points} баллов"""

    def build_negative_feedback(self):
        """ Возвращает:
        \r Ответ неверный, верный ответ __ \n"""
        return f"""Ответ неверный, верный ответ {self.correct_answer}"""
