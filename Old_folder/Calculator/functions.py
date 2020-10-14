from Old_folder.Calculator.input import *


def create_object(label, symbol):
    object = Input(label, symbol)
    object.manage_symbols(label)

