class Input:
	def __init__(self, label, symbol):
		self.label = label
		self.symbol = symbol
		self.result_list = []

	def show_inserted(self, lable, symb):
		lable['text'] = self.symbol
