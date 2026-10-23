#QUEUE i- Linear Queue
# a- isfull |b- isempty|c- enqueue| d-dequeue| e-display|f- peek()


#ex- Queue implementing using queue

class QUEUE:
    def __init__(self,maxsize):
        self.maxsize= maxsize
        self.q1= []

    def IsFull(self):
        if len(self.q1)==self.maxsize:
            return True
        else:
            return False

    def IsEmpty(self):
        if len(self.q1)==0:
            return True
        else:
            return False

    def Enqueue(self,value):
        if self.IsFull():
            print("Queue is Full we can not insert the value now >>")
        else:
            self.q1.append(value)

    def Dequeue(self):
        if self.IsEmpty():
            print('Queue is empty we cannot delete the value')
        else:
            self.q1.pop(0)

    def peek(self):
        if self.IsEmpty():
            print('No elements in Queue')
        else:
            print(self.q1[0])

    def display(self):
        if self.IsEmpty():
            print("No elemets in the queue")
        else:
            print(self.q1)

queue= QUEUE(5)
queue.Enqueue('A')
queue.Enqueue('z')
queue.Enqueue('c')
queue.display()
queue.Dequeue()
queue.peek()
queue.display()
