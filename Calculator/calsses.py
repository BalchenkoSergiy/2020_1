class Calc:
    result = 0

    def __init__(self, result_list):
        self.first = result_list[0]
        self.second = result_list[2]
        self.symbol = result_list[1]

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

