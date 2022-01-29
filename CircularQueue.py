# Circular Queue implementation in Python

class MyCircularQueue():

	def __init__(self,k):
		self.k = k
		self.queue = [None] * k
		self.head = self.tail = -1

	# Insert an element into the Circular Queue
	def enqueue(self, data):
		print(self.k)
		print(self.queue)
		print(self.head)
		print(self.tail)
		if((self.tail + 1) % self.k == self.head):
			print("The Circular Queue is Full\n")

		elif (self.head == -1):
			self.head=0
			self.tail=0
			self.queue[self.tail]=data

		else:
			self.tail = (self.tail + 1) % self.k
			self.queue[self.tail] = data

	#Delete an element from the circular queue
	def dequeue(self):
		if(self.head == -1):
			print("The Circular queue is empty\n")

		elif (self.head == self.tail):
			temp = self.queue[self.head]
			self.head = -1
			self.tail = -1
			return temp

		else:
			temp = self.queue[self.head]
			self.head = (self.head + 1) % self.k
			return temp


	def printCQueue(self):
		if(self.head == -1):
			print("No element in the Circular Queue")

		elif(self.tail >= self.head):
			for i in range(self.head, self.tail + 1):
				print(self.queue[i], end=" ")
			print()
		else:
			for i in range(self.head, self.k):
				print(self.queue[i], end=" ")
			for i in range(0, self.tail + 1):
				print(self.queue[i], end=" ")
			print()



#Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.enqueue(6)
obj.enqueue(7)
obj.enqueue(8)
print("Initial Queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue() 
obj.enqueue(6)
obj.printCQueue() 

