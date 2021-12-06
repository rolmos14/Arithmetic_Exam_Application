import random


class ArithmeticExam:

    def __init__(self, task_quantity):
        self.num_of_tasks = task_quantity
        self.tasks_remaining = task_quantity
        self.correct_answers = 0
        self.level = "1"
        self.level_description = {"1": "simple operations with numbers 2-9",
                                  "2": "integral squares of 11-29"}

    def start(self):
        while True:
            self.level = input(f"Which level do you want? Enter a number:\n"
                               f"1 - {self.level_description['1']}\n"
                               f"2 - {self.level_description['2']}\n")
            if self.level in ["1", "2"]:
                break
            else:
                print("Incorrect format.")
        while self.tasks_remaining:
            result = self.task()
            if result:
                self.correct_answers += 1
            self.tasks_remaining -= 1
        print(f"Your mark is {self.correct_answers}/{self.num_of_tasks}. "
              f"Would you like to save the result? Enter yes or no.")
        if input() in ["yes", "YES", "y", "Yes"]:
            self.save_results()

    def task(self):
        if self.level == "1":
            x = random.randint(2, 9)
            y = random.randint(2, 9)
            operator = random.choice(["+", "-", "*"])
            operation = f'{x} {operator} {y}'
        else:  # self.level == "2"
            x = random.randint(11, 29)
            operation = str(x)
        while True:
            try:
                answer = float(input(f'{operation}\n'))
                break
            except ValueError:
                print("Incorrect format")
        if self.level == "1" and answer == eval(operation) or \
           self.level == "2" and answer == eval(operation + "** 2"):
            print("Right!")
            return True
        else:
            print("Wrong!")
            return False

    def save_results(self):
        user_name = input("What is your name?\n")
        with open("results.txt", "a") as file:
            file.write(f'{user_name}: {self.correct_answers}/{self.num_of_tasks}'
                       f' in level {self.level} ({self.level_description[self.level]})\n')
        print('The results are saved in "results.txt"')


exam = ArithmeticExam(5)
exam.start()
