class ArithmeticExam:

    def __init__(self):
        pass

    def calculate(self, operation):
        return eval(operation)

operation = input()
exam = ArithmeticExam()
print(exam.calculate(operation))
