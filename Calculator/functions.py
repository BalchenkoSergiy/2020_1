from Calculator.input import *
from Calculator.calculator import *


def create_object(label, symbol):
    object = Input(label, symbol)
    object.show_inserted(label, symbol)

