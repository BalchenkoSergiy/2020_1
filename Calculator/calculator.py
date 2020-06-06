class Calc:
    def __init__(self, label, first_number, second_number, operator):
        self.first_number = first_number
        self.second_number = second_number
        self.operator = operator
        self.label = label
        self.calculate_input()


    def calculate_input(self):
        if self.operator == '+':
            self.label['text'] = self.plus()
        elif self.operator == '-':
            self.label['text'] = self.minus()
        elif self.operator == '/':
            self.label['text'] = self.divided()
        elif self.operator == '*':
            self.label['text'] = self.multiply()

    def plus(self):
        return self.first_number + self.second_number

    def minus(self):
        return self.first_number - self.second_number

    def divided(self):
        if int(self.second_number) == 0:
            return 'Oooops! Can`t be ZERO!'
        return self.first_number / self.second_number

    def multiply(self):
        return self.first_number * self.second_number

