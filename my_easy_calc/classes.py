class Calc:
    result = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self):
        global result
        self.result = self.x + self.y
        return self.x + self.y

    def minus(self):
        global result
        self.result = self.x - self.y
        return self.x - self.y

    def divided(self):
        while True:
            try:
                global result
                self.result = self.x / self.y
                return self.x / self.y
            except:
                print('You can`t divided on 0 (zero)!!!')
                self.y = int(input('Try insert other number: '))
            else:
                break

    def multiply(self):
        global result
        self.result = self.x * self.y
        return self.x * self.y


def x():
    while True:
        try:
            var_a = int(input('Insert some first number: '))
            return var_a
        except:
            print('You must insert only integer')
        else:
            break


def y():
    while True:
        try:
            var_b = int(input('Insert some second number: '))
            return var_b
        except:
            print('You must insert only integer')
        else:
            break

