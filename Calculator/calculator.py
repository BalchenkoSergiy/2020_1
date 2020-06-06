class Calc:
    def __init__(self, input):
        self.input = input

    def making_list(self, symbol):
        result = list(symbol)
        return result

    def calculate_input(self, input):
        if len(input) == 3:
            result = calculator.Calc(my_list)
            if my_list[1] == '+':
                label['text'] = f'{result.plus()}'
                return result
            elif my_list[1] == '-':
                label['text'] = f'{result.minus()}'
                return result
            elif my_list[1] == '/':
                if check_zero(label, my_list) != 0:
                    label['text'] = f'{result.divided()}'
                    return result
            elif my_list[1] == '*':
                label['text'] = f'{result.multiply()}'
                return result

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

