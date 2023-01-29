# function to create queue
def CreateQueue():
  queue = []
  return queue

# create function to check whether 
# the queue is empty or not
def isEmpty(queue):
  if(len(queue) == 0):
    print("Queue is empty.")
  else:
    print("Queue is not empty.") 
    
#create function to return size of the queue       
def size(queue):
  print("the size of queue is ",len(queue))

#create function to add new element       
def EnQueue(queue, newElement):
  queue.append(newElement)
  print(newElement, "is added into the queue.")

#create function to delete front element       
def DeQueue(queue):
  print(queue.pop(0), "is deleted from the queue.")

#create function to get front element       
def frontElement(queue):
    print("the Front element is ",queue[0])

#create function to get rear element       
def rearElement(queue):
  print("the last or rear  element ", queue[len(queue) - 1])
        

#test the code                
MyQueue = CreateQueue()

isEmpty(MyQueue)
size(MyQueue)
EnQueue(MyQueue, 10)
EnQueue(MyQueue, 20)
EnQueue(MyQueue, 30)
EnQueue(MyQueue, 40)
size(MyQueue)
frontElement(MyQueue)

DeQueue(MyQueue)
size(MyQueue)
frontElement(MyQueue)

isEmpty(MyQueue)



