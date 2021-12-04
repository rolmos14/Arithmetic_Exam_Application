import random


class ArithmeticExam:

    def __init__(self, task_quantity):
        self.num_of_tasks = task_quantity
        self.tasks_remaining = task_quantity
        self.correct_answers = 0

    def start(self):
        while self.tasks_remaining:
            result = self.task()
            if result:
                self.correct_answers += 1
            self.tasks_remaining -= 1
        print(f"Your mark is {self.correct_answers}/{self.num_of_tasks}")

    def task(self):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operator = random.choice(["+", "-", "*"])
        operation = f'{x} {operator} {y}'
        while True:
            try:
                answer = float(input(f'{operation}\n'))
                break
            except ValueError:
                print("Incorrect format")
        if answer == self.calculate(operation):
            print("Right!")
            return True
        else:
            print("Wrong!")
            return False

    def calculate(self, operation):
        return eval(operation)


exam = ArithmeticExam(5)
exam.start()
