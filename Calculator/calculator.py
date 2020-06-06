class Calc:
    def __init__(self, label, first_number, second_number, operator):
        self.first_number = first_number
        self.second_number = second_number
        self.operator = operator
        self.label = label


    def calculate_input(self, input):
        pass

    def plus(self):
        return float(self.first) + float(self.second)

    def minus(self):
        return float(self.first) - float(self.second)

    def divided(self):
        if self.symbol == '/' and int(self.second) == 0:
            return 0
        return float(self.first) / float(self.second)

    def multiply(self):
        return float(self.first) * float(self.second)

