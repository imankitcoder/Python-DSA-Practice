class NODE:
    def __init__(self,data):
        self.prev= None
        self.data= data
        self.next= None

class Double_Linked_List:
    def __init__(self):
        self.head= None

    def insert_at_last(self,val):
        newNode= NODE(val)
        if self.head is None:
            self.head= newNode
        else:
            temp= self.head
            while temp.next != None:
                temp= temp.next

            temp.next= newNode
            newNode.prev= temp

    def display(self):
            if self.head is None:
                print('No Nodes in DLL')
            else:
                temp= self.head
                while temp:
                    print(temp.data,end= " <=>")
                    temp = temp.next
                print()


    def length(self):
         cnt=0
         temp= self.head
         while temp:
              cnt+=1
              temp=temp.next
         print('The Length of the DLL is', cnt)
    


    def insert_at_first(self,val):
            newNode= NODE(val)
            if self.head is None:
                self.head= newNode
            else:
                newNode.next= self.head
                self.head.prev= newNode


                self.head= newNode

    def insert_at_location(self,val,loc):
         newNode=NODE(val)
         if loc<=0:
              print('enter Loc Above 0')
         elif loc==1:
              self.insert_at_first(val)
         elif loc== self.length()+1:
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
                while temp.next.next !=  None:   #here we give to address
                    temp= temp.next
                temp.next.prev = None
                temp.next= None

    def delete_at_first(self):
                if self.head is None:
                    print('No nodes to remove')
                elif self.length()==1:
                    self.head=None
                else:
                    self.head.next.prev= None
                    self.head= self.head.next



                #hw delete at specified loc

    

dll= Double_Linked_List()

dll.insert_at_last('A')
dll.insert_at_last('B')
dll.insert_at_last('C')
dll.display()
dll.length()
dll.display()
dll.insert_at_first('D')
dll.display()
dll.length()
dll.display()
dll.insert_at_location('E',1)
dll.display()
dll.length()
dll.display()
    