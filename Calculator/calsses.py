class Calc:
    result = 0

    def __init__(self, first_number, symbol, second_number, label='l_first_num'):
        self.first = first_number
        self.second = second_number
        self.symb = symbol
        self.label = label

    # def plus(self):
    #     global result
    #     self.result = self.x + self.y
    #     return int(self.x) + int(self.y)
    #
    # def minus(self):
    #     global result
    #     self.result = self.x - self.y
    #     return self.x - self.y
    #
    # def divided(self):
    #     while True:
    #         try:
    #             global result
    #             self.result = self.x / self.y
    #             return self.x / self.y
    #         except:
    #             print('You can`t divided on 0 (zero)!!!')
    #             self.y = int(input('Try insert other number: '))
    #         else:
    #             break
    #
    # def multiply(self):
    #     global result
    #     self.result = self.x * self.y
    #     return self.x * self.y

