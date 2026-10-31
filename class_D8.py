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
    def length(self):
                if self.head is None:
                    print('No Nodes in single linked list')
                else:
                    # temp= self.head
                    # cnt=0
                    # while temp:
                    #     cnt+=1
                    #     temp= temp.addr
                    # return cnt
                # print(cnt)
                    pass
    def insert_at_first(self,val):
        newNode= Node(val)
        if self.head is None:
            self.head= newNode
            newNode.addr= newNode
        else:
            temp= self.head
            while temp.addr != self.head:
                temp= temp.addr
            temp.addr= newNode
            newNode.addr= self.head
            self.head = newNode

    def insert_at_location(self,loc,val):
              newNode= Node(val)
              if loc<=0:
                  print('enter loc above 0')
              elif loc==1:
                  self.insert_at_first(val)
              elif loc==self.length()+1:
                  self.insertion_at_last(val)
              elif loc>self.length():
                  print('enter loc less than self',self.length())
              else:
                  temp= self.head
                  cnt=1
                  while cnt<loc-1:
                      temp= temp.addr
                      cnt+=1
                  newNode.addr= temp.addr
                  temp.addr= newNode 

    def delete_at_last(self):
            if self.head is None:
                print('No nodes to remove')
            else:
                temp= self.head
                while temp.addr.addr !=  self.head:   #here we give to address
                    temp= temp.addr
                temp.addr= self.head

    def delete_at_first(self):
                if self.head is None:
                    print('No nodes to remove')
                elif self.length()==1:
                    self.head=None
                else:
                    temp= self.head
                    while temp.addr != self.head:
                         temp= temp.addr
                    temp.addr= self.head.addr
                    self.head= self.head.addr

#delete at specified location is same as single linked list
cll= Circular_linked_list()
cll.insertion_at_last(10)
cll.insertion_at_last(20)
cll.insertion_at_last(30)
cll.insertion_at_last(40)
cll.display()
cll.insert_at_first('A')
cll.display()
cll.length()
cll.display()
cll.insert_at_location(1,100)
# cll.insert_at_location(5,500)
# # cll.insert_at_location(3,200)
# # cll.insert_at_location(4,100)
cll.display()
cll.display()
cll.delete_at_last()
cll.display()
cll.delete_at_first()
cll.display()
cll.delete_at_first()
cll.display()