#Queue implementation in Python

class Queue:
	def __init__(self):
		self.queue = []
		self.my_name="Moses Karanja"

	#Add an element
	def enqueue(self, item):
		self.queue.append(item)


	#Remove an element
	def dequeue(self):
		my_var = len(self.queue)
		if len(self.queue) < 1:
			return "Queue is empty"
		return self.queue.pop(0)

	def display(self):
		print(self.queue)

	def display_name(self):
		print(self.my_name)

	def size(self):
		return len(self.queue)



q = Queue()
# print(type(q))
dir(q)
help(q)
q.enqueue(1)
q.enqueue(2)


q.display()

print(q.dequeue())

print(q.dequeue())

print(q.dequeue())

# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()

print("After removing an element.")
print(q.display_name())
q.display()
