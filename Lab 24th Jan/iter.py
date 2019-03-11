import random

class Wow:
	
	def __init__(self, n):
		self.n = n
		self.curr = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.curr >= self.n:
			raise StopIteration()
		self.curr += 1
		return random.randint(0,10)

for x in Wow(10):
	print(x)