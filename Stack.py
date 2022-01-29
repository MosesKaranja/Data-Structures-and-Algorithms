#Stack implementation in python

#Creating a stack
def create_stack():
	#This function creates a stack which we can represent as a list.
	#It then returns that stack.
	stack = []
	return stack;

#Checking if stack is empty
#returns true if stack is empty
def check_empty(stack):
	#This function recieves the stack gotten in function 1 and returns its length.
	#It returns true if the length is 0
	return len(stack) == 0

#Adding items into the stack
def push(stack, item):
	#This function receives the stack and an item. 
	#It then adds that item onto the stack.
	stack.append(item)
	print("Pushed Item: " + item)


#Removing an element from the stack
def pop(stack):
	#This function removes or pops the last element from the stack. 
	if check_empty(stack):
		return "Stack is empty"
	return stack.pop()



stack = create_stack()

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print("Popped Item: " + pop(stack))
print("Check Empty Function: " + str(check_empty(stack)))
print("Stack after popping an element: "+ str(stack))

