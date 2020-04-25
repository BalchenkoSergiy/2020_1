class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 'zero'

    def plus(self):
        self.status = self.x + self.y
        return self.x + self.y

    def minus(self):
        self.status = self.x - self.y
        return self.x - self.y

    def divided(self):
        while True:
            try:
                return self.x / self.y
                self.status = self.x / self.y
            except:
                print('You can`t divided on 0 (zero)!!!')
                self.y = int(input('Try insert other number: '))
            else:
                break

    def multiply(self):
        self.status = self.x * self.y
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