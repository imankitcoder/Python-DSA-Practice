#Circular Linked List

class Node:
    def __init__(self,data):
        self.data= data
        self.addr= None

class Circular_linked_list:
    def __init__(self):
        self.head= None

    
    def insertion_at_last(self,val):
        newNode= Node(val)
        if self.head is None:
            self.head= newNode
            newNode.addr = newNode
        else:
            temp= self.head
            while temp.addr != self.head:

                temp= temp.addr

            temp.addr= newNode
            newNode.addr= self.head
    def display(self):
        if self.head is None:
            print('No Nodes in Circular LL')
        else:
            temp= self.head
            while temp:
                print(temp.data,end= "  <->")
                temp= temp.addr
                if temp ==self.head:
                    break
            print()

cll= Circular_linked_list()
cll.insertion_at_last(10)