#Programm to impliment single linked list inside a stack data structure?
#it should contains Methods Like 
          #push: it should create a Node and then Push the Node to Stack & Head should always Points to the Recently inserted Node.
          #pop: it should remove topmost Node and immediately head should points to its previous nodes
          #peek: It should display Top most Node
          #display: display all the nodes in the form of stack



class Node:
    def __init__(self,data):
        self.data= data
        self.addr= None

class Stack_Linked_List:
    def __init__(self):
        self.head= None

    def push(self,val):
        newNode= Node(val)
        if self.head is None:
            self.head= newNode
        else:
            newNode.addr= self.head
            self.head = newNode

    def display(self):

        if self.head is None:
            print('No Node in Stack')
        else:
            temp= self.head
            while temp:
                print(temp.data)
                temp= temp.addr
    def pop(self):
        if self.head is None:
            print('No nodes in Stack')
        else:
            self.head= self.head.addr

    def peek(self):
        if self.head is None:
            print('No nodes in stak')
        else:
            print('Top noes is ->', self.head.data)



sll= Stack_Linked_List()
sll.push('Apple')
sll.push('Ball')
sll.push('Cat')
sll.display()
