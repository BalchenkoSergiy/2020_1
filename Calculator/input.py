class Input:
	symbols_list = []

	def __init__(self, label, symbol):
		self.label = label
		self.symbol = symbol

	def manage_symbols(self, label):
		self.adding_symbol_to_symbol_list()
		self.show_inserted(label)
		if self.symbol == 'C':
			self.clear_all(label)
		if self.symbol == '=':
			self.join_str_in_list()
			self.split_str()
			self.create_numbers_and_operator(self.symbols_list)
			label['text'] = self.first_number + self.operator + self.second_number
		print(self.symbols_list, type(self.symbols_list))

	def adding_symbol_to_symbol_list(self):
		if self.symbol == '=':
			pass
		else:
			self.symbols_list.append(self.symbol)

	def join_str_in_list(self):
		self.symbols_list = ''.join(map(str, self.symbols_list))

	def split_str(self):
		if '+' in self.symbols_list:
			self.symbols_list = self.symbols_list.split('+', 1)
			self.symbols_list.append('+')
		elif '-' in self.symbols_list:
			self.symbols_list = self.symbols_list.split('-', 1)
			self.symbols_list.append('-')
		elif '/' in self.symbols_list:
			self.symbols_list = self.symbols_list.split('/', 1)
			self.symbols_list.append('/')
		elif '*' in self.symbols_list:
			self.symbols_list = self.symbols_list.split('*', 1)
			self.symbols_list.append('*')

	def show_inserted(self, label):
		label['text'] = ''.join(map(str, self.symbols_list))

	def create_numbers_and_operator(self, list):
		self.first_number = list[0]
		self.second_number = list[1]
		self.operator = list[2]

	def clear_all(self, label):
		self.first_number = 0
		self.second_number = 0
		self.operator = None
		self.symbols_list.clear()
		label['text'] = 'I`m ready to work!!!'