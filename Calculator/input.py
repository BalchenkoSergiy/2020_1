class Input:
	symbols_list = []

	def __init__(self, label, symbol):
		self.label = label
		self.symbol = symbol

	def manage_symbols(self, lable):
		lable['text'] = self.symbol
		self.symbols_list.append(self.symbol)
		self.join_str_in_list()
		self.split_str()

		print(self.symbols_list, type(self.symbols_list))

	def join_str_in_list(self):
		self.symbols_list = ''.join(map(str, self.symbols_list))


	def split_str(self):
		for i in self.symbols_list:
			if i == '+' or i == '-' or i == '/' or i == '*':
				self.symbols_list = self.symbols_list.split(i)
		print(self.symbols_list)
