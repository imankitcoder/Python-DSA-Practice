#circular Doubly Linked List
#it is used to Traverse for multiple tabs in a operation system 
class NODE:
    def __init__(self,data):
        self.prev= None
        self.data= data
        self.next= None

class Circular_Double_Linked_list:
    def __init__(self):
        self.head=None

    def insert_at_last(self,val):
        NewNode=NODE(val)
        if self.head is None:
            self.head=NewNode
            NewNode.next= NewNode
            NewNode.prev=NewNode

        else:
            temp= self.head
            while temp.next != self.head:
                temp= temp.next
            temp.next= NewNode
            NewNode.prev= temp
            NewNode.next= self.head
            self.head.prev= NewNode

    def display(self):
                if self.head is None:
                    print('No Nodes in cdLL')
                else:
                    temp= self.head
                    while temp:
                        print(temp.data,end= " <=>")
                        temp = temp.next
                        if temp== self.head:
                            break
                    print() 

    def length(self):
             if self.head is None:
                  print('No Nodes in cdll to count')
             else:
                  temp= self.head
                  cnt=0
                  while temp:
                       cnt+=1
                       temp= temp.next
                       if temp== self.head:
                            break
                  return cnt


    def insertion_at_first(self,val):
          NewNode= NODE(val)
          if self.head is None:
               self.head=NewNode
               NewNode.next= NewNode
               NewNode.prev=NewNode
          else:
               temp= self.head
               while temp.next!= self.head:
                    temp= temp.next
               temp.next= NewNode
               self.head.prev= NewNode
               NewNode.next= self.head
               NewNode.prev= temp
               self.head= NewNode
    def insert_at_location(self,val,loc):
              newNode=NODE(val)
              if loc<=0:
                   print('enter Loc Above 0')
              elif loc==1:
                   self.insert_at_first(val)
              elif loc== self.length():
                   self.insert_at_last(val)
              elif loc>self.length():
                   print('Enter loc less than', self.length() +1)
              else:
                   temp= self.head
                   cnt=1
                   while cnt<loc -1:
                        temp= temp.next
                        cnt +=1
                   newNode.next= temp.next
                   temp.next.prev= newNode
                   newNode.prev= temp
                   temp.next= newNode  

    def delete_at_last(self):
                if self.head is None:
                    print('No nodes to remove')
                elif self.length()==1:
                     self.head=None
    
                else:
                    temp= self.head
                    while temp.next.next !=  self.head:   #here we give to address
                        temp= temp.next
                    temp.next=self.head
                    temp.head.prev= temp

    def delete_at_first(self):
                    if self.head is None:
                        print('No nodes to remove')
                    elif self.length()==1:
                         self.head=None

                    else:
                          temp= self.head
                          while temp.next!= self.head:
                                temp= temp.next
                          temp.next= self.head.next
                          self.head.next.prev= temp
                          self.head= self.head.next

    def display_next_and_prev(self,val):
          pass

                  
cdll= Circular_Double_Linked_list()        
cdll.insert_at_last('A')
cdll.insert_at_last('B')
cdll.insert_at_last('C')
cdll.display()

cdll.insertion_at_first('D')
cdll.display()
cdll.insert_at_location('f2',4)
cdll.length()
cdll.display()
cdll.delete_at_last()
cdll.display()
cdll.delete_at_first()
cdll.display()