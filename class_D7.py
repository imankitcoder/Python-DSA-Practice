class Node:
    def __init__(self,data):
        self.data= data
        self.addr= None


class Single_linked_List:
    def __init__(self):
        self.head= None

    def insertion_at_last(self,val):
        newNode= Node(val)
        if self.head is None:
            self.head= newNode
        else:
            temp= self.head
            while temp.addr != None:
                temp= temp.addr
            temp.addr= newNode
    def display(self):
        if self.head is None:
            print('No Nodes in single linked list')
        else:
            temp= self.head
            while temp:
                print(temp.data,end= " ->")
                temp = temp.addr
            print()

    def length(self):
            if self.head is None:
                print('No Nodes in single linked list')
            else:
                temp= self.head
                cnt=0
                while temp:
                    cnt+=1
                    temp= temp.addr
                return cnt
            print(cnt)

    def insert_at_first(self,val):
        newNode= Node(val)
        if self.head is None:
            self.head= newNode
        else:
            newNode.addr=self.head
            self.head= newNode

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
            while temp.addr.addr !=  None:   #here we give to address
                temp= temp.addr
            temp.addr= None

    def delete_at_first(self):
            if self.head is None:
                print('No nodes to remove')
            elif self.length()==1:
                self.head=None
            else:
                self.head=self.head.addr

    def delete_at_loc(self,loc):
        if self.head is None:
            print("No Nodes to remove")
        elif loc<=0:
            print('Enter location is above Zero')
        elif loc==1:
            self.delete_at_first()
        elif loc==self.length():
            self.delete_at_last()
        elif loc>self.length():
            print("Enter location lessthan->",self.length())
        else:
            temp=self.head
            cnt= 1
            while cnt<loc-1:
                temp=temp.addr
                cnt +=1
            temp.addr= temp.addr.addr
    #New FUnction of meriging 2 or more linked in one linked list
    
sll= Single_linked_List()
while True:
    print(' single Linked List Operation  ')
    print('1.Insert at last\n 2.Insert at First\n 3. Insert at Loc\n 4. Display\n 5.Length\n 6.Delete at last \n 7.Delete at first\n 8. Delete at Loc')
    opt= int(input('Enter your option: '))
    match opt:
        case 1:
            val= input('enter the value: ')
            sll.insertion_at_last(val)
        case 2:
            val=input('Enter the Value: ')
            sll.insert_at_first(val)
        case 3:
            val=input('Enter the Value: ')
            loc= int(input('Enter the loc: '))
            sll.insert_at_location(loc,val)
        case 4:
            sll.display()
        case 5:
            print('Total Nodes in sll',sll.length())
        case 6:
            sll.delete_at_last()
        case 7:
            sll.delete_at_first()
        case 8:
            loc= int(input('Enter the Loc: '))
            sll.delete_at_loc(loc)
        case _:
            print( 'Invalid Option')
        

# sll= Single_linked_List()
# sll.insertion_at_last(10)
# sll.insertion_at_last(20)
# sll.insertion_at_last(30)

# sll.display()
# sll.length()

# sll.insert_at_first(40)
# sll.display()

# sll.insert_at_location(1,11)
# sll.display()

# sll.insert_at_location(4,'A')
# print(sll.length())

# sll.insert_at_location(7,'B')
# print(sll.length())

# sll.delete_at_last()
# sll.display()
# print(sll.length())


# sll.delete_at_first()
# sll.display
# sll.length()


# sll.delete_at_loc(3)
# sll.display()
# sll.length()