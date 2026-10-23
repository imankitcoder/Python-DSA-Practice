#Circular Queue

class Circular_Queue:
    def __init__(self,maxSize):
        self.maxSize= maxSize
        self.q1= [None]* maxSize
        self.front= -1
        self.rear= -1

    def display(self):
        print(self.q1)

    def IsFull(self):
        if self.front ==0 and self.rear +1 == self.maxSize:
            return True
        elif self.rear +1 == self.front:
            return True
        else:
            False

    def IsEmpty(self):
        if self.front==-1 and self.rear==-1:
            return True
        else:
            return False

    def enqueue(self,val):
        if self.IsFull():
            print("circular is Full")
        else:
            if self.rear +1== self.maxSize:
                self.rear= 0
            else:
                self.rear +=1
                if self.front ==-1:
                    self.front= 0
        self.q1[self.rear]= val

    def dequeue(self):
        idx= self.front
        if self.IsEmpty():
            print("Circular Queue is Empty")
        else:
            if self.front== self.rear:
                self.front= -1
                self.rear= -1
            elif self.front+1== self.maxSize:
                self.front=0
            else:
                self.front+=1
            self.q1[idx]=None

    def peek_ele(self):
        if self.IsEmpty():
            print("Circular Queue is Empty")
        else:
            print("Peek element is ->", self.q1[ self.front])

        

cq= Circular_Queue(5)
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
cq.enqueue("an")
cq.enqueue("ar")
cq.display()
cq.dequeue()
cq.display()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.peek_ele()