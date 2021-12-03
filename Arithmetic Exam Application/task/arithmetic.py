import random


class ArithmeticExam:

    def __init__(self):
        pass

    def task(self):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operator = random.choice(["+", "-", "*"])
        operation = f'{x} {operator} {y}'
        answer = int(input(f'{operation}\n'))
        if answer == self.calculate(operation):
            print("Right!")
        else:
            print("Wrong!")

    def calculate(self, operation):
        return eval(operation)


exam = ArithmeticExam()
exam.task()
