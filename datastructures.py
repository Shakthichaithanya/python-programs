#stack data structure
class stack():
	def __init__(self):
		self.items=[]
	def is_empty(self):
		return not self.items
	def push(self,item):
		return self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def size(self):
		return len(self.items)
	def __str__(self):
		return str(self.items)
		
#queue data structure
from collections import deque
class queue():
	def __init__(self):
		self.items=deque()
	def is_empty(self):
		return not self.items
	def enqueue(self,item):
		return self.items.append(item)
	def dequeue(self):
		return self.items.popleft()
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[0]
	def __str__(self):
		return str(self.items)

